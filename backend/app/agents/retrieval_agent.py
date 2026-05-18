from __future__ import annotations

import asyncio
import json

from rank_bm25 import BM25Okapi
from qdrant_client.models import FieldCondition, Filter, MatchAny

from app.config import settings
from app.embeddings import embed
from app.llm import chat
from app.qdrant_client import get_client
from app.schemas import Chunk

_REWRITE_PROMPT = (
    "The user asked a question that didn't return useful results. Rewrite it as a "
    "more specific, retrieval-friendly query. Keep it short.\n"
    'Return JSON: {{"q": "..."}}\n'
    "Question: {query}"
)


def _tokenize(text: str) -> list[str]:
    return text.lower().split()


class RetrievalAgent:
    def __init__(self) -> None:
        self._bm25: BM25Okapi | None = None
        self._bm25_chunks: list[Chunk] | None = None
        self._bm25_lock = asyncio.Lock()

    async def retrieve(self, role: str | None, query: str, strategy: str, k: int = 5) -> list[Chunk]:
        if strategy == "vector_search":
            return await self._vector(role, query, k)
        if strategy == "rewrite_then_vector":
            return await self._rewrite_vector(role, query, k)
        if strategy == "hybrid_search":
            return await self._hybrid(role, query, k)
        raise ValueError(f"unknown strategy: {strategy}")

    async def _vector(self, role: str | None, query: str, k: int) -> list[Chunk]:
        if role is None:
            raise ValueError("only AccessAgent may bypass role filter")

        vector = await asyncio.to_thread(embed, query)
        client = get_client()

        results = await asyncio.to_thread(
            client.query_points,
            collection_name=settings.COLLECTION_NAME,
            query=vector,
            query_filter=Filter(
                must=[FieldCondition(key="allowed_roles", match=MatchAny(any=[role]))]
            ),
            limit=k,
            with_payload=True,
        )

        return [
            Chunk(
                text=r.payload["text"],
                source_file=r.payload["source_file"],
                source_role=r.payload["source_role"],
                allowed_roles=r.payload["allowed_roles"],
                score=r.score,
            )
            for r in results.points
        ]

    async def _rewrite_vector(self, role: str | None, query: str, k: int) -> list[Chunk]:
        rewritten = query
        try:
            messages = [
                {
                    "role": "user",
                    "content": _REWRITE_PROMPT.format(query=query),
                }
            ]
            raw = await chat(messages, json_mode=True, temperature=0.0)
            data = json.loads(raw)
            rewritten = data.get("q") or query
        except Exception:
            pass
        return await self._vector(role, rewritten, k)

    async def _hybrid(self, role: str | None, query: str, k: int) -> list[Chunk]:
        if role is None:
            raise ValueError("only AccessAgent may bypass role filter")

        await self._ensure_bm25()

        # Vector top-10 (role-filtered by Qdrant)
        vector_chunks = await self._vector(role, query, 10)

        # BM25 top-10 with post-hoc role filter
        tokenized_query = _tokenize(query)
        raw_scores = self._bm25.get_scores(tokenized_query)

        sorted_indices = sorted(range(len(raw_scores)), key=lambda i: raw_scores[i], reverse=True)
        bm25_chunks: list[Chunk] = []
        for idx in sorted_indices:
            chunk = self._bm25_chunks[idx]
            if role in chunk.allowed_roles:
                bm25_chunks.append(Chunk(
                    text=chunk.text,
                    source_file=chunk.source_file,
                    source_role=chunk.source_role,
                    allowed_roles=chunk.allowed_roles,
                    score=float(raw_scores[idx]),
                ))
                if len(bm25_chunks) == 10:
                    break

        # RRF fusion (k=60)
        rrf_k = 60
        rrf_scores: dict[str, float] = {}
        chunk_registry: dict[str, Chunk] = {}

        for rank, chunk in enumerate(vector_chunks, start=1):
            key = chunk.text
            rrf_scores[key] = rrf_scores.get(key, 0.0) + 1.0 / (rrf_k + rank)
            chunk_registry[key] = chunk

        for rank, chunk in enumerate(bm25_chunks, start=1):
            key = chunk.text
            rrf_scores[key] = rrf_scores.get(key, 0.0) + 1.0 / (rrf_k + rank)
            if key not in chunk_registry:
                chunk_registry[key] = chunk

        top_keys = sorted(rrf_scores, key=lambda key: rrf_scores[key], reverse=True)[:k]
        return [chunk_registry[key] for key in top_keys]

    async def _ensure_bm25(self) -> None:
        if self._bm25 is not None:
            return

        async with self._bm25_lock:
            if self._bm25 is not None:  # re-check after acquiring lock
                return

            client = get_client()
            all_chunks: list[Chunk] = []
            offset = None

            while True:
                points, next_offset = await asyncio.to_thread(
                    client.scroll,
                    collection_name=settings.COLLECTION_NAME,
                    limit=250,
                    offset=offset,
                    with_payload=True,
                    with_vectors=False,
                )
                for p in points:
                    all_chunks.append(Chunk(
                        text=p.payload["text"],
                        source_file=p.payload["source_file"],
                        source_role=p.payload["source_role"],
                        allowed_roles=p.payload["allowed_roles"],
                    ))
                if next_offset is None:
                    break
                offset = next_offset

            tokenized_corpus = [_tokenize(c.text) for c in all_chunks]
            self._bm25_chunks = all_chunks
            self._bm25 = BM25Okapi(tokenized_corpus)


retrieval_agent = RetrievalAgent()
