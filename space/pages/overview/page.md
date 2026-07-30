# overview


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_c7ecedc5baa0", "created_at": "2026-07-29T10:17:18+00:00", "title": "In-Context Learning Is Provably Bayesian Inference"}
-->
# In-Context Learning Is Provably Bayesian Inference

OpenReview: https://openreview.net/forum?id=BUFSSOuphA
arXiv: https://arxiv.org/abs/2510.10981

Clean-room CPU reproduction (numpy). A risk identity decomposes total in-context-learning risk into a model-dependent Bayes Gap and an irreducible, model-independent Posterior Variance. For uniform-attention Transformers the Bayes Gap is bounded by an approximation term (m^{−2α/d_eff}) plus an estimation term; the task-type posterior concentrates exponentially in context length; and the Bayes Gap is Wasserstein-stable under input shift.

Verified on a mixture of 3 conjugate Bayesian-linear-regression families (closed-form posterior, no training). 5 anchored claims (10 possible points), all VERIFIED.
