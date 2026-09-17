"""Sema testleri - API anahtari gerektirmez, milisaniyede biter."""
from __future__ import annotations

from datetime import datetime

import pytest
from pydantic import ValidationError

from triage.schemas import (
    AnalyzerOutput,
    Category,
    Decision,
    EmailInput,
    GoldLabel,
    HumanRequired,
)


def _email(**kw) -> EmailInput:
    base = dict(
        message_id="m1",
        from_addr="a@northwind.com",
        subject="test",
        body_text="body",
        received_at=datetime(2026, 9, 17, 9, 0),
        is_external=False,
    )
    base.update(kw)
    return EmailInput(**base)


def test_email_input_is_frozen():
    e = _email()
    with pytest.raises(ValidationError):
        e.subject = "degisti"


def test_thread_context_capped_at_three():
    with pytest.raises(ValidationError):
        _email(prior_messages=["a", "b", "c", "d"])


def test_human_score_must_be_a_probability():
    with pytest.raises(ValidationError):
        AnalyzerOutput(
            summary="s",
            primary=Category.NOISE,
            suggested_decision=Decision.DISCARD,
            human_score_raw=1.4,
            reason="r",
        )


def test_send_is_not_a_valid_decision():
    """v1'de agent'a gonderme yetkisi verilmiyor."""
    assert not hasattr(Decision, "SEND")
    assert set(Decision) == {
        Decision.DISCARD,
        Decision.DELEGATE,
        Decision.DRAFT,
        Decision.HUMAN,
    }


@pytest.mark.parametrize(
    "value,expected",
    [(HumanRequired.YES, True), (HumanRequired.UNCERTAIN, True), (HumanRequired.NO, False)],
)
def test_uncertain_counts_as_human(value, expected):
    """EVALUATION.md, baglayici kural 2."""
    g = GoldLabel(message_id="m1", gold_version="v1", human_required=value)
    assert g.is_human is expected


def test_gold_label_has_no_autonomy_field():
    """Otonomi etiketlenemez - modelin dogrulugundan turetilir."""
    assert "autonomy_mode" not in GoldLabel.model_fields
    assert "human_required" in GoldLabel.model_fields
