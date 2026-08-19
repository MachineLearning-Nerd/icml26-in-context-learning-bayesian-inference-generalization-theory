# Audit report

This repository is an independent reproduction and claim audit for
**In-Context Learning Is Provably Bayesian Inference: A Generalization Theory
for Meta-Learning**.

The risk decomposition, posterior concentration, Wasserstein Bayes-Gap
stability, and exact uniform-attention identity pass their scoped contracts.
Theorem 2 / Claim 2 is falsified as written by a representation collision in
the shared mean-pooled architecture: one and two copies of the same
observation are indistinguishable while their posterior means differ.

Read the detailed report at
[`reports/reproduction/report.md`](reports/reproduction/report.md), the
release report at
[`reports/reproduction/release_report.md`](reports/reproduction/release_report.md),
the evaluator-blind red team at
[`reports/reproduction/evaluator_red_team.md`](reports/reproduction/evaluator_red_team.md),
and the evaluator-facing pages under [`space/pages`](space/pages).

The branch roles and historical `orx/` to clean-name mapping are documented
in [`branch-audit.md`](branch-audit.md). Branch names describe evidence role;
they are not separate paper versions or author statements.

