"""LLM cagrisi. PROJEDEKI TEK NON-DETERMINISTIK MODUL.

Buradan asagisi (policy, router, metrics) saf ve test edilebilir olmali.

CP3'te doldurulacak.
"""
from __future__ import annotations

from .schemas import AnalyzerOutput, EmailInput


def analyze(email: EmailInput, model_id: str) -> tuple[AnalyzerOutput, str, dict]:
    """Donduruyor: (ayristirilmis cikti, HAM yanit, usage).

    Ham yanit RunRecord'a oldugu gibi yazilir - ayristirilmis haliyle degil.
    """
    raise NotImplementedError("CP3")
