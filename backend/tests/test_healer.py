import json
from unittest.mock import AsyncMock, patch

import pytest

from app.agents.healer_agent import healer_agent
from app.schemas import Chunk, Verdict

_CHUNK = Chunk(
    text="The company onboarding process takes two weeks and covers HR policies.",
    source_file="employee_handbook.md",
    source_role="employee",
    allowed_roles=["ceo", "hr", "manager", "employee"],
)

_BASE_VERDICT = Verdict(grounded=False, relevant=False, reason="test failure")


# ---------------------------------------------------------------------------
# 1. Adaptivity — integration, real LLM
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.asyncio
async def test_healer_adaptivity_reads_verdict_reason():
    """Healer picks escalate_to_hybrid or retry_with_rewrite when grader says
    the answer contained pricing data not present in any chunk."""
    verdict = Verdict(
        grounded=False,
        relevant=True,
        reason="answer mentions pricing not in any chunk",
    )
    decision = await healer_agent.decide(
        query="What are the product pricing tiers?",
        strategy="vector_search",
        chunks=[_CHUNK],
        answer="Our pricing starts at $10/month.",
        verdict=verdict,
        strategies_tried=["vector_search"],
    )
    assert decision.action in {"escalate_to_hybrid", "retry_with_rewrite"}
    reasoning_lower = decision.reasoning.lower()
    kws = ["chunk", "term", "keyword", "pric", "exact", "retriev", "miss",
           "hybrid", "rewrite", "ground", "relevan", "rephras", "reformul",
           "support", "context"]
    assert any(kw in reasoning_lower for kw in kws), (
        f"reasoning did not reference retrieval/grounding: {decision.reasoning!r}"
    )


# ---------------------------------------------------------------------------
# 2. No-repeat-strategy — deterministic, mock LLM
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_no_repeat_strategy_override():
    """Safety net: LLM returns retry_vector but vector_search already tried —
    the returned action must NOT be retry_vector."""
    mock_response = json.dumps({"action": "retry_vector", "reasoning": "retry same"})
    with patch("app.agents.healer_agent.chat", new_callable=AsyncMock) as mock_chat:
        mock_chat.return_value = mock_response
        decision = await healer_agent.decide(
            query="test",
            strategy="vector_search",
            chunks=[],
            answer=None,
            verdict=_BASE_VERDICT,
            strategies_tried=["vector_search"],
        )
    assert decision.action != "retry_vector", (
        f"Safety net failed: action was {decision.action!r} "
        "even though vector_search was already tried"
    )


# ---------------------------------------------------------------------------
# 3. Exhausted — deterministic, mock LLM
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_all_strategies_exhausted_gives_check_access():
    """When all three retrieval strategies are exhausted, override to check_access."""
    mock_response = json.dumps({"action": "retry_with_rewrite", "reasoning": "retry"})
    with patch("app.agents.healer_agent.chat", new_callable=AsyncMock) as mock_chat:
        mock_chat.return_value = mock_response
        decision = await healer_agent.decide(
            query="test",
            strategy="hybrid_search",
            chunks=[],
            answer=None,
            verdict=_BASE_VERDICT,
            strategies_tried=["vector_search", "rewrite_then_vector", "hybrid_search"],
        )
    assert decision.action == "check_access"


# ---------------------------------------------------------------------------
# 4. Parse failure — deterministic, mock LLM
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_parse_failure_falls_back_gracefully():
    """Malformed JSON from LLM must not raise; falls back to first unused strategy."""
    with patch("app.agents.healer_agent.chat", new_callable=AsyncMock) as mock_chat:
        mock_chat.return_value = "not json at all"
        decision = await healer_agent.decide(
            query="test",
            strategy="vector_search",
            chunks=[],
            answer=None,
            verdict=_BASE_VERDICT,
            strategies_tried=[],
        )
    assert decision.action == "retry_vector"
    assert "parse error" in decision.reasoning
