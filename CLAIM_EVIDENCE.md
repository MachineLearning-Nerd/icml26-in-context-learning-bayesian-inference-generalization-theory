# Claim-to-evidence ledger

Each verdict is produced by an exact claim contract, source audit, executable
checker, saved raw result, and negative control. The evaluator-facing pages
are under [`space/pages`](space/pages), with mirrored evidence under
[`space/evidence`](space/evidence).

| Claim | Verdict | How the verdict is produced | Primary evidence |
| --- | --- | --- | --- |
| C1. Risk decomposition | `VERIFIED_SCOPED` | Expand squared loss around the conditional mean, cancel the conditional-expectation cross term, and exhaustively check exact rational cases. | [`repro/src/claim1_proof.py`](repro/src/claim1_proof.py) · [`space/evidence/claim1`](space/evidence/claim1) |
| C2. Bayes Gap rate / Theorem 2 | `FALSIFIED_SCOPED` | Set `p=2`, use `f_±(x)=±1`, `x=0`, and noise probabilities `(1/4,1/2,1/4)`; mean pooling maps one and two identical observations to the same representation while Bayes means are `1/3` and `3/5`. | [`repro/src/claim2_counterexample.py`](repro/src/claim2_counterexample.py) · [`repro/src/claim2_independent.py`](repro/src/claim2_independent.py) · [`space/evidence/claim2`](space/evidence/claim2) |
| C3. Posterior concentration | `VERIFIED_SCOPED` | Reconstruct the likelihood-ratio, conditional-MGF, posterior-odds, total-variance, and Bayes-to-minimax proof chain with exact rational checkers. | [`repro/src/claim3_concentration.py`](repro/src/claim3_concentration.py) · [`space/evidence/claim3`](space/evidence/claim3) |
| C4. Wasserstein stability | `VERIFIED_SCOPED` | Derive the encoder/decoder modulus, squared-loss factor, and coupling/Wasserstein step; reject a factor-of-two control and a stronger posterior-variance-invariance reading. | [`repro/src/claim4_stability.py`](repro/src/claim4_stability.py) · [`space/evidence/claim4`](space/evidence/claim4) |
| C5. Uniform attention | `VERIFIED_SCOPED` | Execute the scaled dot-product attention path with `Q=K=0`, exact `Fraction` arithmetic, all permutations at context lengths 1–6, and a nonzero-score control. | [`repro/src/claim5_attention.py`](repro/src/claim5_attention.py) · [`space/evidence/claim5`](space/evidence/claim5) |

The fixed cumulative verifier also checks the protected historical manifest,
release allowlist, evaluator visibility, and tutorial links. The historical
three-family Gaussian experiment is not current evidence.

