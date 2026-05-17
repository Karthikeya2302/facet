"""Run from backend/: python -m app.indexing.ingest [--no-reset]"""
from __future__ import annotations

import argparse
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from qdrant_client.models import PointStruct

from app.config import ROLE_HIERARCHY, settings
from app.embeddings import embed_batch
from app.indexing.chunker import split
from app.qdrant_client import ensure_collection, get_client

DATA_DIR = Path(__file__).parent.parent.parent / "data"
BATCH_SIZE = 64
_PERIOD_SUFFIX = re.compile(r"_(q[1-4]|h[1-2]|\d{4})$")


def _doc_type(stem: str) -> str:
    return _PERIOD_SUFFIX.sub("", stem)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _upsert_batch(client, points: list[PointStruct]) -> None:
    client.upsert(collection_name=settings.COLLECTION_NAME, points=points)


def run(reset: bool) -> None:
    client = get_client()

    if reset:
        print("Resetting collection...")
        try:
            client.delete_collection(settings.COLLECTION_NAME)
        except Exception:
            pass

    ensure_collection()
    print("Collection ready.")

    ingested_at = _now_iso()
    role_counts: dict[str, int] = {}

    for role in ROLE_HIERARCHY:
        role_dir = DATA_DIR / role
        if not role_dir.exists():
            print(f"  [warn] {role_dir} not found — skipping")
            role_counts[role] = 0
            continue

        allowed_roles = ROLE_HIERARCHY[role]
        md_files = sorted(role_dir.glob("*.md"))

        all_chunks: list[tuple[str, str, int]] = []  # (text, source_file, chunk_index)
        for path in md_files:
            text = path.read_text(encoding="utf-8")
            chunks = split(text)
            for idx, chunk in enumerate(chunks):
                all_chunks.append((chunk, path.name, idx))

        if not all_chunks:
            role_counts[role] = 0
            continue

        print(f"  {role}: {len(md_files)} files -> {len(all_chunks)} chunks, embedding...")
        texts = [c[0] for c in all_chunks]
        vectors = embed_batch(texts)

        batch: list[PointStruct] = []
        for (chunk_text, source_file, chunk_index), vector in zip(all_chunks, vectors):
            batch.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={
                        "text": chunk_text,
                        "source_file": source_file,
                        "source_role": role,
                        "allowed_roles": allowed_roles,
                        "doc_type": _doc_type(Path(source_file).stem),
                        "chunk_index": chunk_index,
                        "ingested_at": ingested_at,
                    },
                )
            )
            if len(batch) == BATCH_SIZE:
                _upsert_batch(client, batch)
                batch = []

        if batch:
            _upsert_batch(client, batch)

        role_counts[role] = len(all_chunks)

    print("\nIngest complete:")
    for role, count in role_counts.items():
        print(f"  {role}: {count} chunks")

    total = sum(role_counts.values())
    print(f"  total: {total} chunks")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reset",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="Delete existing collection before upserting (default: true)",
    )
    args = parser.parse_args()
    run(reset=args.reset)


if __name__ == "__main__":
    main()
