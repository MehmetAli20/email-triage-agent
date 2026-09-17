"""Sistemin sozlesmesi. EVALUATION.md ile birlikte okunur.

Iki baglayici kural buraya gomulidur:
  1. GoldLabel agent varliğindan bagimsizdir - registry gercegi degistirmez.
  2. RunRecord ham yaniti OLDUGU GIBI tasir; turetilmis her sey yeniden
     hesaplanabilir olmali.

Modul kohezyona gore bolunur, tipe gore degil. ~500 satiri asarsa
schemas/ paketine donusur ve __init__ hepsini yeniden disa acar; boylece
`from triage.schemas import X` hic degismez.
"""
from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Category(StrEnum):
    """Konuya gore degil, NIYETE gore. Konu kategorileri aksiyonu belirlemiyor."""

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
    """SEND yok - v1'de agent'a gonderme yetkisi verilmiyor."""

    DISCARD = "DISCARD"
    DELEGATE = "DELEGATE"
    DRAFT = "DRAFT"
    HUMAN = "HUMAN"


class HumanRequired(StrEnum):
    YES = "YES"
    NO = "NO"
    UNCERTAIN = "UNCERTAIN"  # birincil metrikte YES sayilir, rapor iki turlu


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
    body_text: str  # temizlenmis: imza, alinti zinciri, dipnot cikarilmis
    received_at: datetime
    is_external: bool  # hesaplanir - sert politika tetikleyicisi
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
    """LLM'in urettigi. human_score_raw KALIBRE DEGIL - modelin beyani."""

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
    """Sert kurallarin ciktisi. Modelin karari degil."""

    blocked: bool
    triggers: list[RiskDomain] = Field(default_factory=list)


class RoutingDecision(BaseModel):
    """Saf fonksiyonun ciktisi: (AnalyzerOutput, PolicyResult, tau) -> bu.

    SAKLANMAZ. Her zaman yeniden hesaplanir, boylece esigi supurmek bedava.
    """

    decision: Decision
    human_score: float  # kalibre edilmis
    threshold: float
    blocked_by: str | None = None
    reason: str


class RunRecord(BaseModel):
    """Degismez ve saklanan TEK sey.

    Eksik yazmanin geri donusu yok: kod her zaman refactor edilebilir,
    kaydedilmeyen veri geri gelmez.
    """

    model_config = ConfigDict(frozen=True)

    run_id: str
    message_id: str
    created_at: datetime

    raw_response: str  # yanitin TAMAMI, ayristirilmadan
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
    """Katman 1 hepsinde, Katman 2 alt kumede.

    DIKKAT: agent varliğindan BAGIMSIZ. Registry degisince bu degismez.
    """

    model_config = ConfigDict(frozen=True)

    message_id: str
    gold_version: str
    human_required: HumanRequired
    importance: Importance = Importance.NORMAL
    tier2_decision: Decision | None = None  # sadece not-HUMAN alt kumesinde
    note: str | None = None

    @property
    def is_human(self) -> bool:
        """UNCERTAIN birincil metrikte YES sayilir (EVALUATION.md, kural 2)."""
        return self.human_required in (HumanRequired.YES, HumanRequired.UNCERTAIN)
