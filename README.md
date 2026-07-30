# Exact reproduction of “In-Context Learning Is Provably Bayesian Inference”

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/blob/main/notebooks/icl_bayesian_reproduction.py)

Paper 2510.10981 claims a shared mean-pooled Transformer ERM has Bayes Gap
tending to zero at the Theorem 2 rate. An exact, assumption-satisfying
counterexample instead proves `R_BG>=1/255` for every model and feature count:
one and two identical observations have the same mean pool but Bayesian means
`1/3` and `3/5`. Theorem 2 is **FALSIFIED** as written. Claims 1, 3, 4, and 5
are **VERIFIED** by universal proof certificates.

There is no toy downscaling or proxy model in the current evidence. Formal
checks used the agreed local compute path: one CPU process, under 0.15 seconds
of verifier runtime per scientific node, no GPU. The previous 3-family
Gaussian proxy is preserved only as a historical rejected baseline.

- [Illustrated technical report](reports/reproduction/report.md)
- [Tutorial marimo notebook](notebooks/icl_bayesian_reproduction.py)
- [Open the notebook in Molab](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/blob/main/notebooks/icl_bayesian_reproduction.py)
- [Evaluator-visible Space candidate](space/pages/current/page.md)

## Experiment log

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `main` | Not run as an experiment (publication surface) | — | reader-facing release | — |
| [`orx/protected-judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/tree/orx/protected-judged-baseline) | Freeze exact judged revision | `uv run --locked python repro/src/verify.py` | 5 historical TOY checks | local CPU, 1 thread |
| [`orx/claim-1-exact-risk-identity`](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/tree/orx/claim-1-exact-risk-identity) | Universal risk identity | `uv run --locked python repro/src/verify.py` | Claim 1 VERIFIED | local CPU, 1 thread |
| [`orx/claim-5-exact-uniform-attention`](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/tree/orx/claim-5-exact-uniform-attention) | Actual scaled-dot-product Q=K=0 path | `uv run --locked python repro/src/verify.py` | Claim 5 VERIFIED | local CPU, 1 thread |
| [`orx/claim-3-exact-posterior-concentration`](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/tree/orx/claim-3-exact-posterior-concentration) | Universal concentration proof | `uv run --locked python repro/src/verify.py` | Claim 3 VERIFIED | local CPU, 1 thread |
| [`orx/claim-4-exact-wasserstein-stability`](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/tree/orx/claim-4-exact-wasserstein-stability) | Universal coupling proof | `uv run --locked python repro/src/verify.py` | Claim 4 VERIFIED | local CPU, 1 thread |
| [`orx/claim-2-cardinality-collision-falsification`](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/tree/orx/claim-2-cardinality-collision-falsification) | Assumption-satisfying collision counterexample | `uv run --locked python repro/src/verify.py` | Claim 2 FALSIFIED | local CPU, 1 thread |

The live judge score is still **5/10**. Any higher total is a forecast until
the published Hugging Face revision is evaluated.
