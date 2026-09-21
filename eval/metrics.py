"""Pure metrics, matching EVALUATION.md section 2 one to one."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Counts:
    tp: int
    fn: int
    fp: int
    tn: int

    @property
    def recall(self) -> float:
        d = self.tp + self.fn
        return self.tp / d if d else float("nan")

    @property
    def fp_rate(self) -> float:
        d = self.fp + self.tn
        return self.fp / d if d else float("nan")

    def expected_cost(self, c_fn: float, c_fp: float) -> float:
        return c_fn * self.fn + c_fp * self.fp


def wilson_ci(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Recall is never reported as a bare point estimate."""
    raise NotImplementedError
