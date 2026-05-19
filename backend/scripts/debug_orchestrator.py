"""Debug script: prints every SSE event for three orchestrator scenarios."""
import asyncio
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.cache import cache
from app.rag.orchestrator import run_query

SCENARIOS = [
    ("ceo",      "what is project nightingale",    "should end with answer"),
    ("employee", "what is project nightingale",    "should end with access_denied"),
    ("ceo",      "what is the company dog's name", "should end with no_info"),
]


async def run_scenario(role: str, query: str, description: str) -> None:
    print(f"\n{'='*70}")
    print(f"SCENARIO: role={role!r}  query={query!r}")
    print(f"EXPECTED: {description}")
    print("="*70)
    cache.clear()
    async for event in run_query(role, query):
        print(json.dumps(event, default=str, ensure_ascii=True))
    print(f"--- end of scenario ---")


async def main() -> None:
    for role, query, desc in SCENARIOS:
        await run_scenario(role, query, desc)


if __name__ == "__main__":
    asyncio.run(main())
