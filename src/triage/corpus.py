"""Korpus temizligi: imza, alinti zinciri, yasal dipnot; is_external hesabi.

CP2'de doldurulacak.
"""
from __future__ import annotations

from pathlib import Path

from .schemas import EmailInput


def clean(raw_path: Path, out_path: Path, internal_domains: list[str]) -> int:
    """Ham .eml -> temizlenmis jsonl. Dondurdugu sey: yazilan mail sayisi."""
    raise NotImplementedError("CP2")


def to_email_input(raw: dict, internal_domains: list[str]) -> EmailInput:
    raise NotImplementedError("CP2")
