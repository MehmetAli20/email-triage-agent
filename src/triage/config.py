"""Sabit yok, konfigurasyon var. Supurulen her sey buradan gelir."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RUNS = ROOT / "runs"
GOLD = DATA / "gold"

# Isletme noktasi - EVALUATION.md, bolum 3
RECALL_FLOOR = 0.95

# Ikincil capraz kontrol. Tek oran SABITLENMEZ.
COST_RATIOS = [20, 50, 100, 200]

# Esik supurme
THRESHOLD_GRID = [i / 100 for i in range(101)]

# Model - maliyet ablasyonunda (CP8) uzerine yazilir
DEFAULT_MODEL = os.getenv("TRIAGE_MODEL", "claude-haiku-4-5")
ABLATION_MODELS = ["claude-opus-5", "claude-sonnet-5", "claude-haiku-4-5"]

GOLD_VERSION = "v1"
HELDOUT_SIZE = 60  # CP8'e kadar acilmaz
