# claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_6db8f60e9280", "created_at": "2026-07-29T10:17:18+00:00", "title": "Claims to reproduce"}
-->
## Claims to reproduce

1. **Proposition 3.1 (risk identity):** the ICL risk decomposes as R(M) = R_BG(M) + R_PV, where R_BG = E[(M − M_Bayes)²] (Bayes Gap, model-dependent) and R_PV = E[Var(f(x_{k+1})|D_k)] (Posterior Variance, irreducible / model-independent).
2. **Theorem 3.2 (Bayes Gap upper bound):** for uniform-attention Transformers, E[R_BG] ≤ m^{−2α/d_eff} (approximation) + Õ(m/(pN) + 1/N) (pretraining generalization); the optimal m⋆ ∝ (pN)^{d_eff/(d_eff+2α)} attains the minimax rate (pN)^{−2α/(d_eff+2α)}.
3. **Theorem 3.3 (posterior concentration):** in a mixture of task types, the posterior over the task index concentrates exponentially on the true index: Pr(I≠i⋆ | D_k) ≤ (T−1) e^{−Ck}.
4. **Theorem 3.4 (Wasserstein stability):** under input-distribution shift, only the Bayes Gap is affected, |R_BG^Q − R_BG^P| ≤ C·W_α(P_X, Q_X); the Posterior Variance is model-independent.
5. **Definition 2.2 (uniform-attention Transformer):** M_θ(P^k) = ρ_θ(mean-pooled ϕ_θ(context), query), permutation-invariant by construction.
