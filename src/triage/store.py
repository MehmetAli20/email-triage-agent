"""RunRecord yaz/oku. Simdilik jsonl; Postgres ANCAK eszamanli yazar olunca.

CP3'te doldurulacak.
"""
from __future__ import annotations

from pathlib import Path

from .schemas import RunRecord


def write(record: RunRecord, path: Path) -> None:
    raise NotImplementedError("CP3")


def read_all(path: Path) -> list[RunRecord]:
    raise NotImplementedError("CP3")
