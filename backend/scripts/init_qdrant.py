"""Run from backend/: python scripts/init_qdrant.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.qdrant_client import count, ensure_collection

if __name__ == "__main__":
    result = ensure_collection()
    print(result)
    print(f"Points in collection: {count()}")
