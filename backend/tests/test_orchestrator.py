"""Integration tests for the orchestrator end-to-end event stream.

All tests hit real Qdrant + Groq. Run with:
    pytest -m integration tests/test_orchestrator.py
"""
from __future__ import annotations

import pytest

from app.rag.cache import cache
from app.rag.orchestrator import run_query

_VALID_HEALER_ACTIONS = frozenset(
    {"retry_with_rewrite", "escalate_to_hybrid", "retry_vector", "check_access", "give_up"}
)


async def _collect(role: str, query: str) -> list[dict]:
    events = []
    async for event in run_query(role, query):
        events.append(event)
    return events


# ---------------------------------------------------------------------------
# 1. Happy path: CEO asks about Project Nightingale → answer
#    vector_search may return off-topic chunks (nightingale brief ranks ~4th),
#    so the healer will escalate to hybrid_search where BM25 keyword matching
#    reliably surfaces the brief.  The test asserts the *eventual* outcome, not
#    the specific number of attempts.
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_ceo_nightingale_happy_path():
    cache.clear()
    events = await _collect("ceo", "what is project nightingale")
    types = [e["type"] for e in events]

    assert types[-1] == "done"
    assert "answer" in types, f"expected 'answer' in event stream, got: {types}"

    assert any(
        e["type"] == "agent_start" and e["agent"] == "retrieval"
        for e in events
    ), "expected at least one agent_start(retrieval)"

    assert any(
        e["type"] == "agent_pass" and e["agent"] == "grader"
        for e in events
    ), "expected agent_pass(grader)"

    assert "cache_write" in types


# ---------------------------------------------------------------------------
# 2. Access denied: employee → access_denied with found_at_role == "ceo"
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_employee_nightingale_access_denied():
    cache.clear()
    events = await _collect("employee", "what is project nightingale")
    types = [e["type"] for e in events]

    assert types[-1] == "done"
    assert "access_denied" in types, f"expected 'access_denied', got: {types}"

    denied = next(e for e in events if e["type"] == "access_denied")
    assert denied["found_at_role"] == "ceo"

    assert sum(1 for t in types if t == "agent_fail") >= 2, (
        "expected ≥2 agent_fail events (at least one grader fail + one access fail)"
    )

    assert "healer_decision" in types


# ---------------------------------------------------------------------------
# 3. No info: CEO asks about company dog → no_info
#    CEO has rank 3 (highest), so the access agent can never find content at a
#    higher role — no_info is structurally guaranteed regardless of retrieval.
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_no_info_for_unknown_query():
    cache.clear()
    events = await _collect("ceo", "what is the company dog's name")
    types = [e["type"] for e in events]

    assert types[-1] == "done"
    assert "no_info" in types, f"expected 'no_info', got: {types}"


# ---------------------------------------------------------------------------
# 4. Cache hit: second run of same CEO query → cache_hit → answer → done, no agents
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_cache_hit_second_run():
    cache.clear()

    # First run — must write to cache
    events1 = await _collect("ceo", "what is project nightingale")
    types1 = [e["type"] for e in events1]
    assert "cache_write" in types1, (
        "first run must produce cache_write for cache-hit test to be valid"
    )

    # Second run — must be a cache hit with no agent activity
    events2 = await _collect("ceo", "what is project nightingale")
    types2 = [e["type"] for e in events2]

    assert types2[0] == "cache_hit"
    assert "answer" in types2
    assert types2[-1] == "done"

    agent_types = {t for t in types2 if t.startswith("agent_")}
    assert not agent_types, (
        f"no agent_* events expected on a cache hit, got: {agent_types}"
    )


# ---------------------------------------------------------------------------
# 5. Healer in sequence: employee-Nightingale → at least one healer_decision
#    with a valid action and non-empty reasoning.
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_healer_decision_in_employee_nightingale_sequence():
    cache.clear()
    events = await _collect("employee", "what is project nightingale")
    healer_events = [e for e in events if e["type"] == "healer_decision"]

    assert len(healer_events) >= 1, (
        "expected at least one healer_decision event in employee-Nightingale sequence"
    )

    for e in healer_events:
        assert e["action"] in _VALID_HEALER_ACTIONS, (
            f"invalid healer action: {e['action']!r}"
        )
        assert isinstance(e["reasoning"], str) and e["reasoning"], (
            "healer_decision must carry non-empty reasoning"
        )
