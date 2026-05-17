"""Run from backend/: python scripts/extract_corpus.py
Parses ../../DEMO_DATA.md and writes each section to data/{role}/{filename}.md.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
DEMO_DATA = REPO_ROOT / "DEMO_DATA.md"
DATA_DIR = Path(__file__).parent.parent / "data"

HEADER_RE = re.compile(r"^## ([a-z]+)/(\S+\.md)$")


def extract(source: Path, out_dir: Path) -> int:
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()

    written = 0
    role = filename = None
    collecting = False
    body: list[str] = []

    def flush():
        nonlocal written
        if role and filename and body:
            dest = out_dir / role / filename
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text("\n".join(body).strip() + "\n", encoding="utf-8")
            print(f"  wrote {dest.relative_to(out_dir.parent)}")
            written += 1

    for line in lines:
        m = HEADER_RE.match(line)
        if m:
            flush()
            body = []
            collecting = False
            role, filename = m.group(1), m.group(2)
            continue

        if role is None:
            continue

        stripped = line.strip()
        if not collecting:
            if stripped.startswith("```"):
                collecting = True
            continue

        # inside a code fence
        if stripped == "```":
            collecting = False
        else:
            body.append(line)

    flush()
    return written


if __name__ == "__main__":
    if not DEMO_DATA.exists():
        print(f"ERROR: {DEMO_DATA} not found", file=sys.stderr)
        sys.exit(1)
    n = extract(DEMO_DATA, DATA_DIR)
    print(f"\nDone — {n} files written to {DATA_DIR}")
