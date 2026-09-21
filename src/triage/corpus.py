"""Corpus cleaning: signatures, quoted chains, legal footers; is_external."""
from __future__ import annotations

from pathlib import Path

from .schemas import EmailInput


def clean(raw_path: Path, out_path: Path, internal_domains: list[str]) -> int:
    """Raw .eml -> cleaned jsonl. Returns the number of emails written."""
    raise NotImplementedError


def to_email_input(raw: dict, internal_domains: list[str]) -> EmailInput:
    raise NotImplementedError
