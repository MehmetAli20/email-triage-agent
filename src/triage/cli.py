"""triage run / triage eval"""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(prog="triage")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="process the corpus, produce RunRecords")
    run.add_argument("--source", default="corpus", choices=["corpus", "gmail"])

    ev = sub.add_parser("eval", help="read records, print metrics")
    ev.add_argument("--gold", default="v1")
    ev.add_argument("--heldout", action="store_true", help="final report only")

    parser.parse_args()
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
