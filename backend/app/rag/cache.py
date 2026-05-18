from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from app.embeddings import embed


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0.0:
        return 0.0
    return float(np.dot(a, b) / denom)


@dataclass
class _Entry:
    role: str
    embedding: np.ndarray
    answer: str


class SemanticCache:
    """In-memory. Key: (role, query embedding). Match by cosine >= threshold."""

    def __init__(self, threshold: float = 0.95) -> None:
        self._threshold = threshold
        self._entries: list[_Entry] = []

    def lookup(self, role: str, query: str) -> str | None:
        if not self._entries:
            return None
        q_vec = np.array(embed(query), dtype=np.float32)
        for entry in self._entries:
            if entry.role != role:
                continue
            if _cosine(q_vec, entry.embedding) >= self._threshold:
                return entry.answer
        return None

    def write(self, role: str, query: str, answer: str) -> None:
        embedding = np.array(embed(query), dtype=np.float32)
        self._entries.append(_Entry(role=role, embedding=embedding, answer=answer))

    def clear(self) -> None:
        self._entries.clear()


cache = SemanticCache()
