# Branch audit

This repository began with OpenResearch-style `orx/` branch names. The clean
names below preserve branch lineage while making the claim or release role
readable. `main` is the publication surface.

| Historical branch | Clean branch | Purpose and evidence scope |
| --- | --- | --- |
| `main` | `main` | Publication README, report, notebook, and cumulative evidence surface. |
| `orx/protected-judged-baseline` | `audit/protected-judged-baseline` | Preserves the historical judged `5/10` toy baseline and protected manifest. |
| `orx/claim-1-exact-risk-identity` | `audit/claim-1-risk-identity` | Exact conditional-expectation risk decomposition and wrong-center control. |
| `orx/claim-2-cardinality-collision-falsification` | `audit/claim-2-cardinality-collision` | Assumption-satisfying mean-pooling collision and exact `1/255` Bayes-Gap lower bound. |
| `orx/claim-3-exact-posterior-concentration` | `audit/claim-3-posterior-concentration` | Universal posterior-odds, concentration, variance, and minimax proof chain. |
| `orx/claim-4-exact-wasserstein-stability` | `audit/claim-4-wasserstein-stability` | Universal coupling proof for Theorem 4 and posterior-variance interpretation control. |
| `orx/claim-5-exact-uniform-attention` | `audit/claim-5-uniform-attention` | Exact scaled-dot-product `Q=K=0` to mean-pooling identity. |
| `orx/evaluator-visible-release-candidate` | `release/evaluator-visible-candidate` | Packages current pages, raw evidence, checkers, controls, and navigation gates. |
| `orx/final-release-gates-and-red-team` | `release/final-gates-red-team` | Records final release gates, repeated evaluator-blind review, and judge-waiting state. |

## Branch hygiene

- No historical `orx/` branch remains in the cleaned public namespace.
- Branch names identify audit or release role and do not determine verdicts.
- The paper-source hash and theorem interpretations are stored in the claim
  contracts and source audits, not inferred from branch names.
- The historical toy baseline remains reachable as provenance but is not used
  for the current claim results.
