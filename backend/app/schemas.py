from dataclasses import dataclass, field
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Shared literals
# ---------------------------------------------------------------------------

AgentName = Literal["retrieval", "generator", "grader", "healer", "access"]

RoleName = Literal["ceo", "hr", "manager", "employee"]

# ---------------------------------------------------------------------------
# Request
# ---------------------------------------------------------------------------


class QueryRequest(BaseModel):
    role: RoleName
    query: str


# ---------------------------------------------------------------------------
# Core domain types
# ---------------------------------------------------------------------------


@dataclass
class Chunk:
    text: str
    source_file: str
    source_role: str
    allowed_roles: list[str] = field(default_factory=list)
    score: float = 0.0


class Verdict(BaseModel):
    grounded: bool
    relevant: bool
    reason: str

    @property
    def passed(self) -> bool:
        return self.grounded and self.relevant


class HealerDecision(BaseModel):
    action: Literal[
        "retry_with_rewrite",
        "escalate_to_hybrid",
        "retry_vector",
        "check_access",
        "give_up",
    ]
    reasoning: str


# ---------------------------------------------------------------------------
# SSE event models — discriminated union on `type`
# ---------------------------------------------------------------------------


class AgentStartEvent(BaseModel):
    type: Literal["agent_start"] = "agent_start"
    agent: AgentName
    label: str
    meta: Optional[dict[str, Any]] = None


class AgentDoneEvent(BaseModel):
    type: Literal["agent_done"] = "agent_done"
    agent: AgentName
    label: str
    meta: Optional[dict[str, Any]] = None


class AgentPassEvent(BaseModel):
    type: Literal["agent_pass"] = "agent_pass"
    agent: AgentName
    label: str
    meta: Optional[dict[str, Any]] = None


class AgentFailEvent(BaseModel):
    type: Literal["agent_fail"] = "agent_fail"
    agent: AgentName
    label: str
    meta: Optional[dict[str, Any]] = None


class HealerDecisionEvent(BaseModel):
    type: Literal["healer_decision"] = "healer_decision"
    action: str
    reasoning: str


class CacheHitEvent(BaseModel):
    type: Literal["cache_hit"] = "cache_hit"


class CacheMissEvent(BaseModel):
    type: Literal["cache_miss"] = "cache_miss"


class CacheWriteEvent(BaseModel):
    type: Literal["cache_write"] = "cache_write"


class AnswerEvent(BaseModel):
    type: Literal["answer"] = "answer"
    text: str


class AccessDeniedEvent(BaseModel):
    type: Literal["access_denied"] = "access_denied"
    found_at_role: str


class NoInfoEvent(BaseModel):
    type: Literal["no_info"] = "no_info"


class ErrorEvent(BaseModel):
    type: Literal["error"] = "error"
    message: str


class DoneEvent(BaseModel):
    type: Literal["done"] = "done"


SSEEvent = Annotated[
    Union[
        AgentStartEvent,
        AgentDoneEvent,
        AgentPassEvent,
        AgentFailEvent,
        HealerDecisionEvent,
        CacheHitEvent,
        CacheMissEvent,
        CacheWriteEvent,
        AnswerEvent,
        AccessDeniedEvent,
        NoInfoEvent,
        ErrorEvent,
        DoneEvent,
    ],
    Field(discriminator="type"),
]
