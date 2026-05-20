from __future__ import annotations

import httpx

from app.config import settings

_JINA_URL = "https://api.jina.ai/v1/embeddings"
_JINA_MODEL = "jina-embeddings-v2-base-en"


def _call(texts: list[str]) -> list[list[float]]:
    with httpx.Client(timeout=30) as client:
        resp = client.post(
            _JINA_URL,
            headers={"Authorization": f"Bearer {settings.JINA_API_KEY}"},
            json={"model": _JINA_MODEL, "input": texts},
        )
        resp.raise_for_status()
    return [item["embedding"] for item in resp.json()["data"]]


def embed(text: str) -> list[float]:
    return _call([text])[0]


def embed_batch(texts: list[str]) -> list[list[float]]:
    return _call(texts)
