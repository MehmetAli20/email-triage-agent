"""Ham skor -> kalibre olasilik.

Modelin beyani BIR GIRDI SINYALIDIR, guven degildir. Guven, o sinyalin
gecmis dogrulukla eslestirilmesinden cikar.

Sizinti uyarisi: kalibratoru fit ettigin dilimde egriyi CIZME.

CP4'te doldurulacak.
"""
from __future__ import annotations


def fit_platt(scores: list[float], labels: list[bool]):
    """Tek ozellikli lojistik regresyon. Ogrendigi sey:
    'model 0.90 dediginde gercekte %72 dogru cikiyor'."""
    raise NotImplementedError("CP4")


def reliability(scores: list[float], labels: list[bool], bins: int = 10):
    """Reliability diagram + ECE. 200 vakada kova basina ~20 ornek -
    tahminler GURULTULU olacak, raporla."""
    raise NotImplementedError("CP4")
