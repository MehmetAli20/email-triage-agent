"""Iki baseline.

1. "her seyi HUMAN'a gonder"  -> bugunku durum, referans noktasi
2. anahtar kelime regex'i     -> LLM'in gecmesi gereken cita

CP2'de doldurulacak.
"""
from __future__ import annotations

KEYWORDS = r"invoice|legal|contract|urgent|payment|deadline|approve"
