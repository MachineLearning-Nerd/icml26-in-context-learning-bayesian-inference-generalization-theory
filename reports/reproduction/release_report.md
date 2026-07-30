- Previous live judged score: `5/10`
- Conservative projected score range after the proposed change: `9–10/10`
- Best-supported possible new score: `10/10` **forecast only; not a judge result**

# Release report

The current live score remains **5/10**. The proposed candidate replaces all
five toy checks with exact terminal verdicts. No score change is claimed before
the live evaluator records the new Hugging Face revision.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 1/2 | 2/2 | HIGH | VERIFIED | Universal conditional-expectation identity, 3,350 exact cases, wrong-center control. Remaining risk: evaluator presentation preference only. |
| 2 | 1/2 | 2/2 | HIGH | FALSIFIED | Every assumption audited; every model has `R_BG>=1/255` while claimed RHS tends to zero; independent closed-form checker. Remaining risk: evaluator interpretation of the theorem’s hidden constants. |
| 3 | 1/2 | 2/2 | HIGH | VERIFIED | Universal MGF, posterior-odds, total-variance, and minimax proof; 4,568 exact checks. Remaining risk: evaluator may ask for a separately formalized concentration lemma. |
| 4 | 1/2 | 2/2 | HIGH | VERIFIED | Universal coupling proof with exact constants; 4,058 checks; invalid posterior-variance invariance reading explicitly rejected. Remaining risk: evaluator may conflate the prose interpretation with the formal theorem. |
| 5 | 1/2 | 2/2 | HIGH | VERIFIED | Actual scaled-dot-product path gives exact `1/k` weights; 873 permutations and nonzero-score control. Remaining risk: evaluator may treat an exact architecture identity as definition-only. |

## Totals and changes

- Current total score: `5/10`
- Conservative projected total score range: `9–10/10`
- Best-supported possible total: `10/10` forecast
- Claims changed since the previous judge result: all five
- Claims remaining BLOCKED: none
- Claim-by-claim confidence: HIGH for Claims 1–5

Claim 2 is not reported as an unsuccessful reproduction. It is a valid
assumption-satisfying falsification of the exact universal statement and is
therefore eligible for full credit under the campaign rubric.

## Experiment tree

The stacked lineage is:

`protected baseline → Claim 1 → Claim 5 → Claim 3 → Claim 4 → Claim 2 falsification → release candidate`

The final release-gate child descends from the release candidate and changes
only evaluator discoverability and release evidence.

The winning scientific branch is
`orx/claim-2-cardinality-collision-falsification` at
`fad5f06e7ee063dc370b14001fdcf88a3244b1f2`. The presentation/release branch
descends from it.

## Formal experiment commands

Every formal node used one fixed reproduction command:

```bash
uv run --locked python repro/src/verify.py
```

Launch commands:

```bash
orx exp run 0ed75c53-651c-40fe-8f9c-707933c59ef4 --backend local
orx exp run 64fb4fd3-ac57-4c24-b73a-ab0dc52552ff --backend local
orx exp run 31609a9c-0487-4ab0-a7ef-63b431c56f41 --backend local
orx exp run 793da3bb-fcd2-4a23-9391-013136e9cebb --backend local
orx exp run 6b3de325-4d0e-451e-ad27-403efaf78f9d --backend local
orx exp run 12795cac-65bd-4eaf-8ff9-63fc77859922 --backend local
orx exp run 3c885d20-4b26-45a0-99d1-26975561bdbc --backend local
orx exp run 696ad22a-431e-44bc-8b55-771cc8e95efa --backend local
```

The verifier runtimes were 0.0258, 0.102255, 0.120083, 0.143983, 0.149517,
0.142646, and 0.150948 seconds through the release-candidate run. Their total
was 0.835232 seconds. Each run was estimated at one CPU core and under one
minute, selected the local CPU backend, and reported one process thread. The
final release-gate runtime is recorded in its OpenResearch run log. External
compute cost: `$0`. Hugging Face CPU runtime and cost: `0`, because no task
crossed the remote-compute threshold.

## Evidence paths

- Canonical evaluator page: `space/pages/current/page.md`
- Self-contained Space verifier: `space/repro/src/verify.py`
- Claim evidence: `space/evidence/claim1` through `space/evidence/claim5`
- Internal durable evidence: `.openresearch/artifacts/claim1` through
  `.openresearch/artifacts/claim5`
- Illustrated report: `reports/reproduction/report.md`
- Tutorial notebook: `notebooks/icl_bayesian_reproduction.py`
- Protected judged manifest:
  `.openresearch/artifacts/baseline/protected_space_manifest.sha256`

## Publication action

After the candidate-download traversal, subset/hash check, secret scan,
allowlist construction, and repeated evaluator-blind red team all pass, the
exact action will be:

1. upload the text allowlist to the existing Space `DineshAI/BUFSSOuphA`;
2. verify the returned Hugging Face revision by downloading it and rerunning
   the canonical traversal;
3. fast-forward or merge the presentation artifacts to GitHub `main`, push,
   and confirm the remote SHA with `git ls-remote`;
4. mark the paper awaiting judge without claiming a score change.

No second Space will be created.
