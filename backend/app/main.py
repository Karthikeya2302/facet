from __future__ import annotations

import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from app.config import settings
from app.qdrant_client import count
#from app.rag.orchestrator import run_query
from app.schemas import QueryRequest

app = FastAPI(title="Facet")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN, "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/query")
async def query(req: QueryRequest) -> EventSourceResponse:
    async def event_generator():
        async for event in run_query(role=req.role, query=req.query):
            yield {"data": json.dumps(event)}

    return EventSourceResponse(event_generator())


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "qdrant_chunks": count()}

async def run_query(role: str, query: str):
    yield {"data": "mock"}