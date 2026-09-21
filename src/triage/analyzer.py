"""The LLM call. THE ONLY NON-DETERMINISTIC MODULE IN THE PROJECT.

Everything downstream of this (policy, router, metrics) stays pure and testable.
"""
from __future__ import annotations

from .schemas import AnalyzerOutput, EmailInput


def analyze(email: EmailInput, model_id: str) -> tuple[AnalyzerOutput, str, dict]:
    """Returns (parsed output, RAW response, usage).

    The raw response is written to the RunRecord verbatim, not in parsed form.
    """
    raise NotImplementedError
