import pytest

from app.agents.retrieval_agent import retrieval_agent


@pytest.mark.parametrize("role,forbidden_files", [
    ("employee", {"project_nightingale_brief.md", "exec_compensation.md",
                  "regulatory_inquiry_response.md", "salary_bands_2025.md",
                  "payments_team_roadmap_h1.md"}),
    ("manager",  {"project_nightingale_brief.md", "salary_bands_2025.md",
                  "regulatory_inquiry_response.md"}),
    ("hr",       {"project_nightingale_brief.md", "regulatory_inquiry_response.md",
                  "fundraise_plans_2026.md"}),
])
@pytest.mark.parametrize("strategy", ["vector_search", "rewrite_then_vector", "hybrid_search"])
@pytest.mark.asyncio
async def test_role_filter_never_leaks(role, forbidden_files, strategy):
    queries = [
        "project nightingale acquisition",
        "executive compensation structure",
        "engineering salary bands",
        "payments team roadmap",
        "regulatory inquiry from central bank",
    ]
    for q in queries:
        chunks = await retrieval_agent.retrieve(role=role, query=q, strategy=strategy, k=10)
        leaked = {c.source_file for c in chunks} & forbidden_files
        assert not leaked, f"role={role} q={q!r} strategy={strategy} leaked {leaked}"


@pytest.mark.asyncio
async def test_ceo_can_see_everything():
    chunks = await retrieval_agent.retrieve(role="ceo", query="project nightingale", strategy="vector_search", k=5)
    assert any(c.source_file == "project_nightingale_brief.md" for c in chunks)


@pytest.mark.asyncio
async def test_role_none_raises():
    with pytest.raises(ValueError):
        await retrieval_agent.retrieve(role=None, query="anything", strategy="vector_search")
