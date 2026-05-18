import pytest

from app.agents.grader_agent import grader_agent
from app.schemas import Chunk


_CHUNKS = [
    Chunk(
        text="The company has a standard 20 vacation days policy for all full-time employees.",
        source_file="employee_handbook.md",
        source_role="employee",
        allowed_roles=["ceo", "hr", "manager", "employee"],
    )
]

_QUERY = "How many vacation days do employees get?"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_hallucinated_answer_not_grounded():
    hallucinated = (
        "Employees receive 45 vacation days per year plus 15 bonus days "
        "that can be rolled over indefinitely."
    )
    verdict = await grader_agent.judge(_QUERY, hallucinated, _CHUNKS)
    assert verdict.grounded is False


@pytest.mark.integration
@pytest.mark.asyncio
async def test_supported_answer_passes():
    good_answer = "Employees receive 20 vacation days per year according to company policy."
    verdict = await grader_agent.judge(_QUERY, good_answer, _CHUNKS)
    assert verdict.grounded is True
    assert verdict.relevant is True
