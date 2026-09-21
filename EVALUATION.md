# Measurement Contract

**Status: FROZEN.** Nothing in the "Frozen" table below may change after
results have been seen. If it does, every label and every number is void.

Unit of evaluation: **one email**. Positive class: **HUMAN**.

## 1. Label definition

`human_required = YES` if **any** of these hold:

- It needs a decision or an authorisation only I can give
- It creates or refers to a commitment or a deadline
- Not responding has a cost (money, legal, relationship, missed opportunity)
- It carries something I would **want to know**, even with no action required

`human_required = NO` if **all** of these hold:

- No action is needed from me
- No decision is needed from me
- Nothing is lost if it disappears entirely

### Two binding rules

1. **The label is independent of agent availability.** The registry never
   changes the truth. Consequence: delegating a gold `HUMAN` email is
   **always** an error.
2. If you cannot decide, label it **`UNCERTAIN`**. It counts as `YES` in the
   primary metric, and the report shows the numbers **both ways**.

### Borderline cases - annotation guide

| Case | Label | Reason |
|---|---|---|
| Newsletter announcing a breaking API change | `YES` | I need to know; missing it has a cost |
| Cold recruiter email | `YES` | High value right now - the label is time-dependent |
| Optional meeting invite | `YES` | The RSVP is a decision only I can make |
| CC'd on a thread, no question for me | **depends** | YES if it's my area, NO if it's pure CC noise |
| CI failure on a repo I own | `YES` | I want to know. The system may say DELEGATE; gold stays YES |
| Invoice FYI copy, already approved | `NO` | No action, no decision. Hard policy still catches it - deliberate |

## 2. Metrics

```
TP = gold HUMAN,     predicted HUMAN
FN = gold HUMAN,     predicted not-HUMAN     <- the expensive one
FP = gold not-HUMAN, predicted HUMAN
TN = gold not-HUMAN, predicted not-HUMAN

HUMAN recall      = TP / (TP + FN)        <- HEADLINE, always with a CI
missed rate       = FN / (TP + FN) = 1 - recall
FP rate           = FP / (FP + TN)        <- reweighted to true prevalence
expected cost     = c_FN * FN + c_FP * FP
AUC                                        <- auxiliary only
```

**High-importance recall is reported separately.** Recall is never written as
a point estimate - a Wilson confidence interval is mandatory.

## 3. Operating point

- **Primary rule:** minimise FP subject to `recall >= 0.95`.
- **Secondary (cross-check):** `argmin(c_FN*FN + c_FP*FP)`, computed separately
  for cost ratios **20:1, 50:1, 100:1, 200:1**.

A single cost ratio is **never fixed**. `tau*` is plotted as a function of the
ratio: stable means the choice is robust, unstable is itself a finding.

## 4. Exclusions

Cases blocked by hard policy do **not** enter the threshold curve. They are
reported separately with their own precision. Reason: they do not test
"did the model pick the right threshold", they test "does the policy catch them".

## 5. Data

```
Gold set        ~250, DELIBERATELY IMBALANCED: ~150 HUMAN candidates + ~100 not-HUMAN
                (representative sampling is the wrong design here - estimating
                 recall needs enough POSITIVES, not the true distribution)
Prevalence      ~100 emails, RANDOM and unstratified -> estimate of pi
                (required to turn FP rate into "unnecessary emails per day")
Held-out        60 emails, NOT OPENED until the final report. Headline numbers
                are reported on this slice.
Versioning      gold_version. Corrections are allowed; the version increments
                and the whole evaluation is re-run.
```

## 6. Frozen / changeable

| Frozen | Changeable |
|---|---|
| Label definition | Model |
| The two binding rules | Prompt |
| Metric formulas | Threshold (tau) |
| Positive class | Feature set |
| Exclusion rule | Calibrator |
| Operating-point rule, R = 0.95 | Gold set contents *(version bump)* |
| Held-out slice | |

## 7. Scope limit

One inbox, one annotator, one period. Results are specific to that person and
that window.

**The learned layer is personal; the hard policy is universal.** The cold
recruiter email is the proof: `YES` today, probably `NO` in six months.
