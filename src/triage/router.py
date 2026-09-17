"""Karar yonlendirici. SAF fonksiyon.

tau ve kalibre skor disaridan gelir - bu modul hicbir sey ogrenmez ve
hicbir yan etki uretmez. Sayesinde esik supurme bedava.

CP3'te doldurulacak.
"""
from __future__ import annotations

from .schemas import AnalyzerOutput, PolicyResult, RoutingDecision


def route(
    analyzer: AnalyzerOutput,
    policy: PolicyResult,
    human_score: float,
    threshold: float,
    registry: dict,
) -> RoutingDecision:
    """Sira onemli: once sert politika, sonra guven esigi, sonra registry.

    Registry'de agent yoksa -> HUMAN, blocked_by="target_agent_unavailable".
    """
    raise NotImplementedError("CP3")
