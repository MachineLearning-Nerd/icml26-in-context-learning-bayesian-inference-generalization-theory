# Source audit

The claim contracts use the arXiv HTML retrieved on `2026-07-30` for
**In-Context Learning Is Provably Bayesian Inference: A Generalization Theory
for Meta-Learning**.

| Field | Value |
| --- | --- |
| Source | https://ar5iv.labs.arxiv.org/html/2510.10981 |
| SHA-256 | `6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1` |
| Claim anchors | Theorems 1–4 and Definition 2 |
| Scope | Exact statements and shared mean-pooled architecture in the audited source |

Claim 2's collision uses the architecture's mean pooling exactly. Because the
same feature average is produced for one repeated observation and two
repeated observations, no width or feature-map choice can remove the
collision without adding cardinality information. The exact weighted
optimization gives Bayes Gap at least `1/255`.

Claim 4 verifies the Bayes-Gap shift bound only; it does not assert that
posterior variance is invariant between source and target input laws. Claim 5
audits the exact `Q=K=0` uniform-attention identity rather than an empirical
training result.

Detailed per-claim assumptions and interpretation controls are under
[`space/evidence`](space/evidence) and `.openresearch/artifacts`.

