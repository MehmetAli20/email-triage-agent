"""Decision router. A PURE function.

The threshold and the calibrated score are passed in - this module learns
nothing and has no side effects, which is why sweeping the threshold is free.
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
    """Order matters: hard policy first, then the confidence gate, then the registry.

    If the target agent is unavailable -> HUMAN, blocked_by="target_agent_unavailable".
    """
    raise NotImplementedError
