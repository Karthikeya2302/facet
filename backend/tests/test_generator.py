import pytest

from app.rag.generator import generate
from app.schemas import Chunk


@pytest.mark.integration
@pytest.mark.asyncio
async def test_generate_returns_nonempty_string():
    chunks = [
        Chunk(
            text="The company offers 20 vacation days per year to all full-time employees.",
            source_file="employee_handbook.md",
            source_role="employee",
            allowed_roles=["ceo", "hr", "manager", "employee"],
        )
    ]
    result = await generate("How many vacation days do employees get?", chunks, "employee")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
