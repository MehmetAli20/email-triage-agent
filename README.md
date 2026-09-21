# Email Triage Agent

A risk-aware routing agent for a corporate inbox. Its job is not to write
replies - it is to decide **who should take control of this email**.

```
DISCARD    don't surface it to the user (archive, never delete)
DELEGATE   hand off to another agent (checked against the registry)
DRAFT      prepare a reply, don't send it
HUMAN      must reach the user
```

There is no `SEND` decision. v1 gives the agent no authority to send anything.

## Research question

> How much human email workload can an LLM routing agent remove, while
> keeping the rate of missed human-required email below a stated ceiling?

Constraint first, optimisation second. The measurement contract is in
[EVALUATION.md](EVALUATION.md) and is frozen.

## Three layers

| Layer | Question | Role |
|---|---|---|
| **HUMAN?** | Should this reach me? | The measurable contribution |
| **WHO?** | If not, who handles it? | The architecture |
| **HOW?** | What gets done? | Extensibility |

## Architecture boundary

`analyzer.py` is the only non-deterministic module. `policy.py`, `router.py`
and `eval/metrics.py` stay pure - if you find `import anthropic` in any of
them, the boundary has slipped.

`RoutingDecision` is **never persisted**; it is recomputed on every read.
That is what makes sweeping the threshold free. `RunRecord` is frozen and
carries the full raw response alongside the model id, prompt hash and git sha.

## Setup

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e ".[dev]"
.venv/Scripts/python.exe -m pytest
```

## Status

Evaluation contract frozen, skeleton in place. Progress log: [NOTES.md](NOTES.md)
