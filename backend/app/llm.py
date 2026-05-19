from __future__ import annotations

import asyncio
import re

from groq import AsyncGroq, APIConnectionError, APITimeoutError, RateLimitError

from app.config import settings

_client: AsyncGroq | None = None

_DEFAULT_RATE_LIMIT_SLEEP = 65  # fallback seconds when no retry-after found


def _parse_retry_after(error_msg: str) -> float:
    """Parse 'Please try again in Xm Y.Zs' from Groq rate-limit messages."""
    m = re.search(r"try again in (?:(\d+)m\s*)?(\d+(?:\.\d+)?)s", error_msg)
    if m:
        mins = int(m.group(1) or 0)
        secs = float(m.group(2))
        return mins * 60 + secs + 5  # 5-second buffer
    return _DEFAULT_RATE_LIMIT_SLEEP


def _get_client() -> AsyncGroq:
    global _client
    if _client is None:
        _client = AsyncGroq(api_key=settings.GROQ_API_KEY)
    return _client


async def chat(
    messages: list[dict],
    json_mode: bool = False,
    temperature: float = 0.0,
) -> str:
    client = _get_client()
    kwargs: dict = dict(model=settings.GROQ_MODEL, messages=messages, temperature=temperature)
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}

    for attempt in range(3):
        try:
            resp = await client.chat.completions.create(**kwargs)
            return resp.choices[0].message.content
        except RateLimitError as exc:
            if attempt >= 2:
                raise
            wait = _parse_retry_after(str(exc))
            await asyncio.sleep(wait)
        except (APIConnectionError, APITimeoutError):
            if attempt >= 2:
                raise
