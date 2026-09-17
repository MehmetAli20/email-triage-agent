"""triage run / triage eval

CP2-CP3'te doldurulacak.
"""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(prog="triage")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="korpusu isle, RunRecord uret")
    run.add_argument("--source", default="corpus", choices=["corpus", "gmail"])

    ev = sub.add_parser("eval", help="kayitlari oku, metrikleri bas")
    ev.add_argument("--gold", default="v1")
    ev.add_argument("--heldout", action="store_true", help="CP8'e kadar kullanma")

    args = parser.parse_args()
    raise NotImplementedError(f"{args.cmd}: CP2-CP3")


if __name__ == "__main__":
    raise SystemExit(main())
