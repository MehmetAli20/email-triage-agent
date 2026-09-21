"""Raw score -> calibrated probability.

What the model asserts is an input signal, not a confidence. Confidence comes
from matching that signal against observed correctness.

Leakage warning: do not plot the curve on the slice the calibrator was fit on.
"""
from __future__ import annotations


def fit_platt(scores: list[float], labels: list[bool]):
    """Single-feature logistic regression. What it learns:
    'when the model says 0.90 it is actually right 72% of the time'."""
    raise NotImplementedError


def reliability(scores: list[float], labels: list[bool], bins: int = 10):
    """Reliability diagram and ECE. With 200 cases a bin holds ~20 samples -
    the estimates will be noisy, so report that."""
    raise NotImplementedError
