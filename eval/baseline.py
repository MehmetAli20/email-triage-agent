"""Two baselines.

1. "send everything to HUMAN" - the status quo, and the reference point
2. a keyword regex       - the bar the LLM has to clear
"""
from __future__ import annotations

KEYWORDS = r"invoice|legal|contract|urgent|payment|deadline|approve"
