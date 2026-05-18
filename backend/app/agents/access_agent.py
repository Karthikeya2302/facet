from __future__ import annotations

import asyncio

from app.config import ROLE_RANK, settings
from app.embeddings import embed
from app.qdrant_client import get_client
from app.schemas import Chunk


class AccessAgent:
    async def check(self, query: str, current_role: str) -> str | None:
        """Returns the higher role at which content exists, or None."""
        chunks = await self._unfiltered_search(query, k=3)
        if not chunks:
            return None
        top_role = chunks[0].source_role
        if ROLE_RANK[top_role] > ROLE_RANK[current_role]:
            return top_role
        return None

    async def _unfiltered_search(self, query: str, k: int) -> list[Chunk]:
        # Security carve-out: this is the ONLY place in the codebase that
        # performs unfiltered Qdrant retrieval (no allowed_roles filter).
        # Encapsulated here so it can be audited in one place. The result is
        # used only to determine whether content exists at a higher access
        # level — the chunk text is never surfaced to the end user.
        vector = await asyncio.to_thread(embed, query)
        client = get_client()

        results = await asyncio.to_thread(
            client.query_points,
            collection_name=settings.COLLECTION_NAME,
            query=vector,
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


access_agent = AccessAgent()
