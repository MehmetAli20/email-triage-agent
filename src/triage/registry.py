"""Agent registry. No downstream agent is implemented - only the interface
and the routing decision that depends on it.
"""
from __future__ import annotations

import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def is_available(registry: dict, agent: str | None) -> bool:
    if not agent:
        return False
    return bool(registry.get(agent, {}).get("available"))
