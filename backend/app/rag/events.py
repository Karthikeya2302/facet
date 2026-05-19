from __future__ import annotations

from typing import Any


def agent_start(agent: str, label: str, meta: dict[str, Any] | None = None) -> dict:
    event: dict[str, Any] = {"type": "agent_start", "agent": agent, "label": label}
    if meta is not None:
        event["meta"] = meta
    return event


def agent_done(agent: str, label: str, meta: dict[str, Any] | None = None) -> dict:
    event: dict[str, Any] = {"type": "agent_done", "agent": agent, "label": label}
    if meta is not None:
        event["meta"] = meta
    return event


def agent_pass(agent: str, label: str, meta: dict[str, Any] | None = None) -> dict:
    event: dict[str, Any] = {"type": "agent_pass", "agent": agent, "label": label}
    if meta is not None:
        event["meta"] = meta
    return event


def agent_fail(agent: str, label: str, meta: dict[str, Any] | None = None) -> dict:
    event: dict[str, Any] = {"type": "agent_fail", "agent": agent, "label": label}
    if meta is not None:
        event["meta"] = meta
    return event


def healer_decision(action: str, reasoning: str) -> dict:
    return {"type": "healer_decision", "action": action, "reasoning": reasoning}


def cache_hit() -> dict:
    return {"type": "cache_hit"}


def cache_miss() -> dict:
    return {"type": "cache_miss"}


def cache_write() -> dict:
    return {"type": "cache_write"}


def answer(text: str) -> dict:
    return {"type": "answer", "text": text}


def access_denied(found_at_role: str) -> dict:
    return {"type": "access_denied", "found_at_role": found_at_role}


def no_info() -> dict:
    return {"type": "no_info"}


def error(msg: str) -> dict:
    return {"type": "error", "message": msg}


def done() -> dict:
    return {"type": "done"}
