# Reproduction status

## Paper

**In-Context Learning Is Provably Bayesian Inference: A Generalization
Theory for Meta-Learning** by Tomoya Wakayama and Taiji Suzuki. The source
audit records arXiv `2510.10981` and its exact retrieved HTML hash.

## Overall verdict

`PARTIAL_CLAIMS_1_3_4_5_VERIFIED_CLAIM_2_THEOREM_2_FALSIFIED`

Claims 1, 3, 4, and 5 pass exact symbolic or architecture contracts. Theorem
2 / Claim 2 is falsified as written for the shared mean-pooled decoder: one
copy and two copies of the same observation have the same representation,
but different Bayesian posterior means. The exact Bayes Gap lower bound is
`1/255`, while the claimed upper bound tends to zero along
`m_N=ceil(sqrt(N))`.

## Claim boundary

`C1_C3_C4_C5_SCOPED_VERIFIED_C2_SHARED_MEAN_POOL_THEOREM2_CARDINALITY_COLLISION_FALSIFIED`

This does not falsify a cardinality-aware or sum-pooling decoder, nor a
theorem restricted to one fixed context length. The historical Gaussian
experiment is retained as rejected baseline context and is not used for the
current verdicts.

| Item | Status |
| --- | --- |
| Current score claim | `false` |
| Publication gate | `false` |
| Official author endorsement | `false` |
| Last historical live judge | `5/10` |
| Projected score | `9/10–10/10`, forecast only |

## Verification

The cumulative evidence was produced with:

```bash
uv sync --locked
uv run --locked python repro/src/verify.py
```

The exact contracts, raw outputs, independent checkers, negative controls,
source audits, and release gates are linked from
[`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md).

