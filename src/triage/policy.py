"""Sert politika kapisi. SAF - modelin karari buraya karismaz.

Buraya `import anthropic` girerse mimari sinir kaymis demektir.

CP3'te doldurulacak.
"""
from __future__ import annotations

from .schemas import AnalyzerOutput, EmailInput, PolicyResult


def evaluate(email: EmailInput, analyzer: AnalyzerOutput) -> PolicyResult:
    """Finansal / hukuki / guvenlik / dis aksiyon -> HUMAN, esikten bagimsiz.

    Bloklanan vakalar esik egrisine GIRMEZ (EVALUATION.md, bolum 4).
    """
    raise NotImplementedError("CP3")
