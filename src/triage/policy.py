"""Hard policy gate. PURE - the model's opinion does not reach in here.

If `import anthropic` ever appears in this file, the architecture boundary
has slipped.
"""
from __future__ import annotations

from .schemas import AnalyzerOutput, EmailInput, PolicyResult


def evaluate(email: EmailInput, analyzer: AnalyzerOutput) -> PolicyResult:
    """Financial / legal / security / external-action -> HUMAN, regardless of score.

    Blocked cases are excluded from the threshold curve (EVALUATION.md, section 4).
    """
    raise NotImplementedError
