from __future__ import annotations

from typing import AsyncIterator

from app.agents.access_agent import access_agent
from app.agents.grader_agent import grader_agent
from app.agents.healer_agent import ACTION_TO_STRATEGY, healer_agent
from app.agents.retrieval_agent import retrieval_agent
from app.rag.cache import cache
from app.rag.events import (
    access_denied,
    agent_done,
    agent_fail,
    agent_pass,
    agent_start,
    answer,
    cache_hit,
    cache_miss,
    cache_write,
    done,
    error,
    healer_decision,
    no_info,
)
from app.rag.generator import generate
from app.schemas import Verdict

MAX_ATTEMPTS = 3


def _action_to_strategy(action: str) -> str:
    return ACTION_TO_STRATEGY[action]


async def run_query(role: str, query: str) -> AsyncIterator[dict]:
    try:
        # ---- Cache check ----
        hit = cache.lookup(role, query)
        if hit:
            yield cache_hit()
            yield answer(hit)
            yield done()
            return
        yield cache_miss()

        strategies_tried: list[str] = []
        current_strategy = "vector_search"
        attempt = 0

        while attempt < MAX_ATTEMPTS:
            attempt += 1

            # ---- Retrieval Agent ----
            yield agent_start("retrieval", f"Retrieval Agent — {current_strategy}")
            chunks = await retrieval_agent.retrieve(
                role=role, query=query, strategy=current_strategy, k=5
            )
            strategies_tried.append(current_strategy)
            if not chunks:
                yield agent_fail("retrieval", f"{current_strategy} — 0 chunks")
                decision = await healer_agent.decide(
                    query=query,
                    strategy=current_strategy,
                    chunks=[],
                    answer=None,
                    verdict=Verdict(grounded=False, relevant=False, reason="no chunks"),
                    strategies_tried=strategies_tried,
                )
                yield healer_decision(decision.action, decision.reasoning)
                if decision.action in ("check_access", "give_up"):
                    break
                current_strategy = _action_to_strategy(decision.action)
                continue
            yield agent_done("retrieval", f"{current_strategy} — {len(chunks)} chunks")

            # ---- Generator ----
            yield agent_start("generator", "Generating answer")
            ans = await generate(query, chunks, role)
            yield agent_done("generator", "Answer generated")

            # ---- Grader Agent ----
            yield agent_start("grader", "Grading (grounded + relevant)")
            verdict = await grader_agent.judge(query, ans, chunks)
            if verdict.passed:
                yield agent_pass("grader", "Grounded ✓ Relevant ✓")
                cache.write(role, query, ans)
                yield cache_write()
                yield answer(ans)
                yield done()
                return
            yield agent_fail("grader", verdict.reason)

            # ---- Healer Agent ----
            yield agent_start("healer", "Picking recovery action")
            decision = await healer_agent.decide(
                query=query,
                strategy=current_strategy,
                chunks=chunks,
                answer=ans,
                verdict=verdict,
                strategies_tried=strategies_tried,
            )
            yield agent_done("healer", f"Chose: {decision.action}")
            yield healer_decision(decision.action, decision.reasoning)

            if decision.action in ("check_access", "give_up"):
                break
            current_strategy = _action_to_strategy(decision.action)

        # ---- Access Agent ----
        yield agent_start("access", "Checking access level")
        higher = await access_agent.check(query=query, current_role=role)
        if higher:
            yield agent_fail("access", f"Content exists at {higher} level")
            yield access_denied(found_at_role=higher)
        else:
            yield agent_done("access", "No matching content")
            yield no_info()
        yield done()
    except Exception as exc:
        yield error(str(exc))
        yield done()
