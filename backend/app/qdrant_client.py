from __future__ import annotations

from qdrant_client import QdrantClient
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.models import Distance, PayloadSchemaType, VectorParams

from app.config import settings

_client: QdrantClient | None = None


def get_client() -> QdrantClient:
    global _client
    if _client is None:
        _client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )
    return _client


def ensure_collection() -> str:
    client = get_client()
    name = settings.COLLECTION_NAME

    existing = {c.name for c in client.get_collections().collections}
    if name not in existing:
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

    try:
        client.create_payload_index(
            collection_name=name,
            field_name="allowed_roles",
            field_schema=PayloadSchemaType.KEYWORD,
        )
    except UnexpectedResponse:
        pass  # index already exists

    return f"Collection '{name}' ready with allowed_roles index."


def count() -> int:
    return get_client().count(collection_name=settings.COLLECTION_NAME).count
