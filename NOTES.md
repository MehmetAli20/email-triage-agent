# Decision Log

Three lines per step: **what was done - what number came out - what was decided**.
This file is the project's memory once a working session ends.

---

## 2026-09-17 - contract frozen, skeleton up

**Done:** Skeleton created. Measurement contract frozen as `EVALUATION.md`.
Schema written. 8 tests passing, 2 skipped, ruff clean.

**Decision - autonomy cannot be labelled.** The first design put an
`autonomy_mode` label in the gold set. That label cannot exist: "could this
have been handled without me" is not a property of the email, it is a
consequence of whether the model got it right. Replaced with the binary
`HUMAN / not-HUMAN`, which *is* a property of the email and can be annotated
directly.

**Decision - the label ignores agent availability.** If gold changed when the
registry changed, the gold set would be unstable.

**Decision - R = 0.95, held-out slice 60 emails, informational email is
`YES` when I would want to know.**

**Next:** corpus cleaning and the first 30 labels.
