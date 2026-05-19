from __future__ import annotations

import json

from app.llm import chat
from app.schemas import Chunk, Verdict

_PROMPT = (
    "You are a strict evaluator. Given a question, an answer, and the source chunks "
    "used to produce it, decide:\n\n"
    "1. grounded: is every factual claim in the answer supported by at least one "
    "chunk? If the answer introduces any fact not present in any chunk, grounded is false. "
    "Synthesising facts from multiple chunks is acceptable provided no new fact is added.\n"
    "2. relevant: does the answer actually address the question? "
    "IMPORTANT: An answer that says the information 'is not in the context', "
    "'cannot be answered', 'not mentioned', 'I cannot answer', or any equivalent "
    "disclaimer does NOT address the question — mark relevant=false for such answers.\n\n"
    'Return JSON only:\n{{"grounded": true|false, "relevant": true|false, "reason": "one short sentence"}}\n\n'
    "Question: {query}\n"
    "Answer: {answer}\n"
    "Chunks:\n{chunks}"
)

_FALLBACK = Verdict(grounded=False, relevant=False, reason="grader parse error")


class GraderAgent:
    async def judge(self, query: str, answer: str, chunks: list[Chunk]) -> Verdict:
        chunks_text = "\n\n".join(
            f"[source: {c.source_file}]\n{c.text}" for c in chunks
        )
        messages = [
            {
                "role": "user",
                "content": _PROMPT.format(query=query, answer=answer, chunks=chunks_text),
            }
        ]
        try:
            raw = await chat(messages, json_mode=True, temperature=0.0)
            data = json.loads(raw)
            return Verdict(
                grounded=bool(data["grounded"]),
                relevant=bool(data["relevant"]),
                reason=str(data["reason"]),
            )
        except (json.JSONDecodeError, KeyError, TypeError):
            return _FALLBACK


grader_agent = GraderAgent()
