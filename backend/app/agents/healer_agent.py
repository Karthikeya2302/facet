from __future__ import annotations

import json
from typing import Optional

from app.llm import chat
from app.schemas import Chunk, HealerDecision, Verdict

ACTION_TO_STRATEGY: dict[str, str] = {
    "retry_with_rewrite": "rewrite_then_vector",
    "escalate_to_hybrid": "hybrid_search",
    "retry_vector":       "vector_search",
}

_STRATEGY_TO_ACTION: dict[str, str] = {v: k for k, v in ACTION_TO_STRATEGY.items()}

_CANONICAL_STRATEGIES = ["vector_search", "rewrite_then_vector", "hybrid_search"]

_VALID_ACTIONS = frozenset(ACTION_TO_STRATEGY) | {"check_access", "give_up"}

_PROMPT_TEMPLATE = (
    "You are the Healer Agent in a multi-agent RAG system. The retrieval+answer\n"
    "pipeline just failed. Decide what to do next.\n\n"
    "Query: {query}\n"
    "Strategy attempted: {strategy}\n"
    "Strategies already tried this query: {strategies_tried}\n"
    "Number of chunks retrieved: {num_chunks}\n"
    "Sample chunk excerpts: {excerpts}\n"
    "Generated answer: {answer_text}\n"
    "Grader verdict: grounded={grounded} relevant={relevant}\n"
    "Grader reason: {reason}\n\n"
    "Choose ONE action:\n"
    "- retry_with_rewrite: query is ambiguous or uses unusual phrasing; reformulating may surface better chunks\n"
    "- escalate_to_hybrid: chunks look related but miss exact terms; keyword+vector hybrid may help\n"
    "- retry_vector: previous attempt had a transient issue; retry vanilla vector\n"
    "- check_access: pattern strongly suggests content does not exist for this role\n"
    "- give_up: all reasonable strategies exhausted\n\n"
    "Hard rules:\n"
    "- Do not pick a strategy that's already in {strategies_tried}.\n"
    "- If 2+ strategies have been tried and grader keeps failing, prefer check_access or give_up.\n\n"
    "Return JSON only:\n"
    '{{"action": "...", "reasoning": "one short sentence"}}'
)


def _next_action(strategies_tried: list[str]) -> str:
    for strategy in _CANONICAL_STRATEGIES:
        if strategy not in strategies_tried:
            return _STRATEGY_TO_ACTION[strategy]
    return "check_access"


class HealerAgent:
    async def decide(
        self,
        query: str,
        strategy: str,
        chunks: list[Chunk],
        answer: Optional[str],
        verdict: Verdict,
        strategies_tried: list[str],
    ) -> HealerDecision:
        excerpts = (
            " | ".join(c.text[:120] for c in chunks[:3]) if chunks else "none"
        )
        answer_text = answer if answer else "(no answer — retrieval returned nothing)"

        prompt = _PROMPT_TEMPLATE.format(
            query=query,
            strategy=strategy,
            strategies_tried=strategies_tried,
            num_chunks=len(chunks),
            excerpts=excerpts,
            answer_text=answer_text,
            grounded=verdict.grounded,
            relevant=verdict.relevant,
            reason=verdict.reason,
        )

        messages = [{"role": "user", "content": prompt}]

        try:
            raw = await chat(messages, json_mode=True, temperature=0.0)
            data = json.loads(raw)
            action = str(data["action"])
            if action not in _VALID_ACTIONS:
                action = _next_action(strategies_tried)
                return HealerDecision(action=action, reasoning=str(data.get("reasoning", "")))
            decision = HealerDecision(action=action, reasoning=str(data["reasoning"]))
        except (json.JSONDecodeError, KeyError, TypeError):
            return HealerDecision(
                action=_next_action(strategies_tried),
                reasoning="healer parse error — fell back to linear order",
            )

        # Code-level safety net: if chosen action maps to an already-tried strategy, override
        if decision.action in ACTION_TO_STRATEGY:
            if ACTION_TO_STRATEGY[decision.action] in strategies_tried:
                return HealerDecision(
                    action=_next_action(strategies_tried),
                    reasoning=decision.reasoning,
                )

        return decision


healer_agent = HealerAgent()
