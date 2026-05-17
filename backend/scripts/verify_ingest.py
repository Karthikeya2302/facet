"""Run from backend/: python scripts/verify_ingest.py"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import ROLE_HIERARCHY, settings
from app.qdrant_client import get_client


def main() -> None:
    client = get_client()

    # Fetch all points (corpus is small) and group by source_role in Python.
    all_points, _ = client.scroll(
        collection_name=settings.COLLECTION_NAME,
        limit=1000,
        with_payload=True,
    )
    by_role: dict[str, list] = {r: [] for r in ROLE_HIERARCHY}
    for p in all_points:
        sr = (p.payload or {}).get("source_role")
        if sr in by_role:
            by_role[sr].append(p)

    failures: list[str] = []

    for role, expected_allowed in ROLE_HIERARCHY.items():
        results = by_role[role]

        if not results:
            print(f"[{role}] WARNING: no points found — was ingest run?")
            continue

        point = random.choice(results)
        payload = point.payload or {}
        source_role = payload.get("source_role", "<missing>")
        allowed_roles = payload.get("allowed_roles", [])

        print(f"[{role}]  id={point.id}")
        print(f"         source_role   = {source_role!r}")
        print(f"         allowed_roles = {allowed_roles!r}")
        print(f"         expected      = {expected_allowed!r}")

        if sorted(allowed_roles) != sorted(expected_allowed):
            msg = f"  FAIL: allowed_roles mismatch for role={role!r}"
            print(msg)
            failures.append(msg)
        else:
            print(f"  OK")
        print()

    if failures:
        print("Verification FAILED:")
        for f in failures:
            print(f)
        sys.exit(1)
    else:
        print("All assertions passed.")


if __name__ == "__main__":
    main()
