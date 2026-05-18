from unittest.mock import MagicMock, patch

import pytest

from app.agents.access_agent import AccessAgent

_FAKE_VECTOR = [0.0] * 384


def _make_point(source_role: str) -> MagicMock:
    point = MagicMock()
    point.payload = {
        "text": "some text",
        "source_file": "file.md",
        "source_role": source_role,
        "allowed_roles": ["ceo"] if source_role == "ceo" else ["ceo", "hr", "manager", "employee"],
    }
    point.score = 0.9
    return point


def _qdrant_response(*source_roles: str) -> MagicMock:
    resp = MagicMock()
    resp.points = [_make_point(r) for r in source_roles]
    return resp


@pytest.mark.asyncio
async def test_employee_nightingale_returns_ceo():
    """Employee querying CEO-only content → returns 'ceo'."""
    agent = AccessAgent()
    client_mock = MagicMock()
    client_mock.query_points.return_value = _qdrant_response("ceo", "ceo", "employee")

    with patch("app.agents.access_agent.embed", return_value=_FAKE_VECTOR), \
         patch("app.agents.access_agent.get_client", return_value=client_mock):
        result = await agent.check(query="project nightingale", current_role="employee")

    assert result == "ceo"


@pytest.mark.asyncio
async def test_employee_vacation_returns_none():
    """Employee querying employee-level content → returns None (not restricted)."""
    agent = AccessAgent()
    client_mock = MagicMock()
    client_mock.query_points.return_value = _qdrant_response("employee", "employee", "employee")

    with patch("app.agents.access_agent.embed", return_value=_FAKE_VECTOR), \
         patch("app.agents.access_agent.get_client", return_value=client_mock):
        result = await agent.check(query="vacation days", current_role="employee")

    assert result is None


@pytest.mark.asyncio
async def test_ceo_vacation_returns_none():
    """CEO querying employee-level content → returns None (top_role not higher than ceo)."""
    agent = AccessAgent()
    client_mock = MagicMock()
    client_mock.query_points.return_value = _qdrant_response("employee", "employee", "employee")

    with patch("app.agents.access_agent.embed", return_value=_FAKE_VECTOR), \
         patch("app.agents.access_agent.get_client", return_value=client_mock):
        result = await agent.check(query="vacation days", current_role="ceo")

    assert result is None
