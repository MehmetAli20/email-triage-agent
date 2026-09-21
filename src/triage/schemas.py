"""The system's contract. Read alongside EVALUATION.md.

Two binding rules are baked in here:
  1. GoldLabel is independent of agent availability - the registry never
     changes the truth.
  2. RunRecord carries the raw response verbatim, so anything derived from it
     can be recomputed without calling the model again.

Modules are split by cohesion, not by type. If this file passes ~500 lines it
becomes a schemas/ package whose __init__ re-exports everything, so
`from triage.schemas import X` keeps working either way.
"""
from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Category(StrEnum):
    """By intent, not by topic. Topic categories don't determine the action."""

    REQUEST_ACTION = "REQUEST_ACTION"
    REQUEST_INFO = "REQUEST_INFO"
    APPROVAL_NEEDED = "APPROVAL_NEEDED"
    STATUS_UPDATE = "STATUS_UPDATE"
    ESCALATION = "ESCALATION"
    SCHEDULING = "SCHEDULING"
    AUTOMATED = "AUTOMATED"
    NOISE = "NOISE"


class RiskDomain(StrEnum):
    FINANCIAL = "FINANCIAL"
    LEGAL = "LEGAL"
    SECURITY = "SECURITY"
    EXTERNAL_ACTION = "EXTERNAL_ACTION"
    TECHNICAL = "TECHNICAL"
    NONE = "NONE"


class Decision(StrEnum):
    """No SEND - v1 gives the agent no authority to send anything."""

    DISCARD = "DISCARD"
    DELEGATE = "DELEGATE"
    DRAFT = "DRAFT"
    HUMAN = "HUMAN"


class HumanRequired(StrEnum):
    YES = "YES"
    NO = "NO"
    UNCERTAIN = "UNCERTAIN"  # counts as YES in the primary metric; reported both ways


class Importance(StrEnum):
    HIGH = "HIGH"
    NORMAL = "NORMAL"


class EmailInput(BaseModel):
    model_config = ConfigDict(frozen=True)

    message_id: str
    thread_id: str | None = None
    from_addr: str
    to_addrs: list[str] = Field(default_factory=list)
    cc_addrs: list[str] = Field(default_factory=list)
    subject: str
    body_text: str  # cleaned: signature, quoted chain and footer stripped
    received_at: datetime
    is_external: bool  # computed - one of the hard-policy triggers
    thread_position: int = 1
    prior_messages: list[str] = Field(default_factory=list, max_length=3)
    has_attachments: bool = False


class ExtractedFields(BaseModel):
    reference_ids: list[str] = Field(default_factory=list)
    requester: str | None = None
    deadline: str | None = None
    amount: str | None = None
    mentioned_systems: list[str] = Field(default_factory=list)


class AnalyzerOutput(BaseModel):
    """What the LLM produces. human_score_raw is NOT calibrated - it is what
    the model asserts about itself."""

    summary: str
    primary: Category
    secondary: list[Category] = Field(default_factory=list)
    fields: ExtractedFields = Field(default_factory=ExtractedFields)
    risk_domain: RiskDomain = RiskDomain.NONE
    suggested_decision: Decision
    target_agent: str | None = None
    human_score_raw: float = Field(ge=0.0, le=1.0)
    reason: str


class PolicyResult(BaseModel):
    """Output of the hard rules. Not the model's decision."""

    blocked: bool
    triggers: list[RiskDomain] = Field(default_factory=list)


class RoutingDecision(BaseModel):
    """Output of a pure function: (AnalyzerOutput, PolicyResult, tau) -> this.

    NEVER PERSISTED. Recomputed every time, which is what makes sweeping the
    threshold free.
    """

    decision: Decision
    human_score: float  # calibrated
    threshold: float
    blocked_by: str | None = None
    reason: str


class RunRecord(BaseModel):
    """The only thing that is immutable and stored.

    Getting this wrong is the one unrecoverable mistake: code can always be
    refactored, data that was never recorded is gone.
    """

    model_config = ConfigDict(frozen=True)

    run_id: str
    message_id: str
    created_at: datetime

    raw_response: str  # the response in full, unparsed
    analyzer: AnalyzerOutput
    policy: PolicyResult

    model_id: str
    prompt_hash: str
    schema_version: str
    policy_version: str
    git_sha: str

    input_tokens: int
    output_tokens: int
    latency_ms: int


class GoldLabel(BaseModel):
    """Tier 1 on every case, tier 2 on a subset.

    NOTE: independent of agent availability. Changing the registry does not
    change this.
    """

    model_config = ConfigDict(frozen=True)

    message_id: str
    gold_version: str
    human_required: HumanRequired
    importance: Importance = Importance.NORMAL
    tier2_decision: Decision | None = None  # only on the not-HUMAN subset
    note: str | None = None

    @property
    def is_human(self) -> bool:
        """UNCERTAIN counts as YES in the primary metric (EVALUATION.md, rule 2)."""
        return self.human_required in (HumanRequired.YES, HumanRequired.UNCERTAIN)
