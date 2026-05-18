from __future__ import annotations

from groq import AsyncGroq, APIConnectionError, APITimeoutError, RateLimitError

from app.config import settings

_client: AsyncGroq | None = None


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

    for attempt in range(2):
        try:
            resp = await client.chat.completions.create(**kwargs)
            return resp.choices[0].message.content
        except (APIConnectionError, APITimeoutError, RateLimitError):
            if attempt == 1:
                raise
