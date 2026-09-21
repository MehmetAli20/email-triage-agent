"""Configuration, not constants. Anything that gets swept lives here."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RUNS = ROOT / "runs"
GOLD = DATA / "gold"

# Operating point - EVALUATION.md, section 3
RECALL_FLOOR = 0.95

# Secondary cross-check. A single ratio is never fixed.
COST_RATIOS = [20, 50, 100, 200]

THRESHOLD_GRID = [i / 100 for i in range(101)]

# Overridden during the cost ablation
DEFAULT_MODEL = os.getenv("TRIAGE_MODEL", "claude-haiku-4-5")
ABLATION_MODELS = ["claude-opus-5", "claude-sonnet-5", "claude-haiku-4-5"]

GOLD_VERSION = "v1"
HELDOUT_SIZE = 60  # not opened until the final report
