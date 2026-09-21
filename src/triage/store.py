"""Read and write RunRecords. jsonl for now; Postgres only once there are
concurrent writers.
"""
from __future__ import annotations

from pathlib import Path

from .schemas import RunRecord


def write(record: RunRecord, path: Path) -> None:
    raise NotImplementedError


def read_all(path: Path) -> list[RunRecord]:
    raise NotImplementedError
