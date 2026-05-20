# Facet Backend

FastAPI backend for the Facet multi-agent RBAC RAG system.

## Prerequisites

- Python 3.11+
- A Qdrant Cloud free-tier cluster
- A Groq API key

## Install

```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -e .
```

## Configure

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `QDRANT_URL` | Your Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant API key |
| `GROQ_API_KEY` | Groq API key |
| `COLLECTION_NAME` | Qdrant collection name (default: `company_docs`) |
| `CORS_ORIGIN` | Your Vercel frontend URL |
| `GROQ_MODEL` | Groq model ID (default: `llama-3.3-70b-versatile`) |
| `EMBED_MODEL` | Sentence-transformers model (default: `all-MiniLM-L6-v2`) |

## Run dev server

```bash
uvicorn app.main:app --reload --port 10000
```

## Run tests

```bash
pytest
```

Tests require a `.env` with valid credentials, or set env vars directly:

```bash
QDRANT_URL=... QDRANT_API_KEY=... GROQ_API_KEY=... CORS_ORIGIN=http://localhost:3000 pytest
```

## Smoke test (local)

Start the dev server:

```bash
uvicorn app.main:app --reload --port 10000
```

Then in a separate terminal:

```bash
# CEO can see Project Nightingale
curl -N -X POST http://localhost:10000/query \
  -H "Content-Type: application/json" \
  -d '{"role": "ceo", "query": "what is project nightingale"}'

# Employee gets access_denied
curl -N -X POST http://localhost:10000/query \
  -H "Content-Type: application/json" \
  -d '{"role": "employee", "query": "what is project nightingale"}'

# Health check
curl http://localhost:10000/health
```

Each `/query` response is a `text/event-stream` where every frame is `data: {json}\n\n`.
The `done` event signals end of stream. See §7 of `ARCHITECTURE.md` for the full event protocol.

## Deploy to Render

The `render.yaml` blueprint is in this directory. Render expects blueprints at
the repository root — copy or symlink it there before connecting the repo:

```bash
cp backend/render.yaml render.yaml
```

Then connect the GitHub repo in the Render dashboard and select
**"Use existing render.yaml"**. Set the secret env vars
(`QDRANT_URL`, `QDRANT_API_KEY`, `GROQ_API_KEY`, `CORS_ORIGIN`) in the
Render dashboard after deployment.
