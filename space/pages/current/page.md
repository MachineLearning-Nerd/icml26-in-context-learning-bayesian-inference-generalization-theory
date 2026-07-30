# Current verification

This page is the canonical evaluator entrypoint. It supersedes the verifier in
the judged revision `b604006ac298769e9dcee6ecb42b45369eb68cce`.

## Claim 2 — FALSIFIED

**Exact source statement.** Theorem 2 claims that the one ERM shared across
every `k=1,...,p` has expected Bayes Gap bounded, up to fixed constants, by

`m^(-2alpha/d_eff)+m/(pN)polylog(pN)+N^(-1)polylog(pN)`.

**Assumption-satisfying counterexample.** Fix `p=2`, `d_feat=1`, `d_eff=2`,
and one task type whose function prior is uniform on constant bounded
functions `f_+(x)=1`, `f_-(x)=-1`. Inputs are identically zero. I.i.d. noise
has masses `1/4,1/2,1/4` at `-2,0,2`; it is centered, has variance 2, and
`E exp(lambda epsilon)=cosh²(lambda)<=exp(lambda²)`. Exact enumeration of 212
positive-probability prompt pairs gives a common Hölder version with
`alpha=1`, `L=1`; a symmetrized Lipschitz extension covers zero-probability
sequences.

For observation `y=1`, exact Bayes means `1/3` and `3/5` occur after one and
two repetitions, with probabilities `3/8` and `5/32`. But Definition 2 gives
both contexts the same representation:

`phi(0,1)=[phi(0,1)+phi(0,1)]/2`.

Thus every `theta` and every `m` must use one prediction on both events. The
best such prediction is `7/17`, yielding the **uniform lower bound `1/255`**
on average Bayes Gap. It applies to every realized ERM, so also after
expectation over training data.

**Contradiction.** With `m_N=ceil(sqrt(N))`, `p=2`, `d_eff=2`, `alpha=1`,
all three claimed RHS terms tend to zero for every fixed polylog exponent and
implicit constant, contradicting `E R_BG>=1/255`.

**Proof gap and controls.** Lemma 5 constructs a decoder separately for each
fixed `k`; the theorem requires one decoder across all `k`, while mean pooling
does not encode cardinality. Giving `k` to the decoder makes the collision
loss exactly zero. Making the observation equally likely under both tasks
also makes the two posterior means equal, so both controls remove the
counterexample for the intended reason.

**Downloadable evidence.**

- [Claim contract](../../evidence/claim2/claim_contract.json)
- [Raw counterexample](../../evidence/claim2/raw_counterexample.json)
- [Independent checker output](../../evidence/claim2/independent_checker_output.json)
- [Negative-control output](../../evidence/claim2/negative_control_output.json)
- [Executable source](../../evidence/claim2/claim2_counterexample.py)
- [Independent closed-form source](../../evidence/claim2/claim2_independent.py)
- [Method](../../evidence/claim2/method.md)
- [Limitations](../../evidence/claim2/limitations.md)

## Claim 1 — VERIFIED

**Exact source statement.** Under Definition 1 and Assumption 1, for every
measurable bounded predictor `M`, Theorem 1 states
`R(M)=R_BG(M)+R_PV`, averaged over every `k=1,…,p`.

**Why the full quantifier is covered.** For an arbitrary conditional law of
`F=f(x_{k+1})` given a prompt, set `mu=E[F|prompt]`. Exact expansion gives

`(M-F)^2-(M-mu)^2-(F-mu)^2 = 2(M-mu)(mu-F)`.

Conditionally, `M` and `mu` are fixed and `E[mu-F|prompt]=0`; hence the
cross-term vanishes for every admissible conditional law. Averaging over
prompts and `k` is exactly the theorem. No Gaussian family, Monte Carlo
tolerance, chosen dimension, or fitted sample size is involved.

**Independent checker.** Exact rational arithmetic checked **3,350 exact
rational cases**, with zero failures, across support sizes 1–3, all positive
rational weights of denominator at most 4, values and predictions in
`{-2,-1,0,1,2}`.

**Negative control.** Replacing the conditional mean by `mu+1/2` while omitting
the cross-term gives exact residual `-3/2`; the checker rejects it.

**Command and compute.**

```bash
uv run --locked python repro/src/verify.py
```

Python `3.12.*`, no third-party dependencies, deterministic, no seed. Estimated
and selected: one local CPU core, under one minute. Formal run metadata will be
copied here after the OpenResearch run.

**Downloadable evidence.**

- [Claim contract](../../evidence/claim1/claim_contract.json)
- [Raw proof certificate](../../evidence/claim1/raw_proof.json)
- [Independent checker output](../../evidence/claim1/independent_checker_output.json)
- [Negative-control output](../../evidence/claim1/negative_control_output.json)
- [Executable source](../../evidence/claim1/claim1_proof.py)
- [Method](../../evidence/claim1/method.md)
- [Limitations](../../evidence/claim1/limitations.md)

## Claim 5 — VERIFIED

**Exact source statement.** Definition 2 sets `Q=K=0` and defines
`M_theta(P^k)=rho_theta(k^{-1} sum_i phi_theta(x_i,y_i),x_{k+1})`.

**Actual attention mechanism.** The executable follows the scaled dot-product
path. Zero queries and keys give zero scores; `exp(0)=1`, so softmax assigns
exact weight `1/k` to each `V_i=phi_theta(x_i,y_i)`. Thus attention output is
the displayed mean pool identically, before the decoder receives it and the
query.

**Independent checker.** Exact rational arithmetic verified equality and
uniform weights for **873 exact context permutations** at lengths 1–6, with
zero failures.

**Negative control.** Scores `[0,1]` yield weights
`0.268941421369995…` and `0.731058578630004…`; the checker rejects this as
uniform attention.

**Downloadable evidence.**

- [Claim contract](../../evidence/claim5/claim_contract.json)
- [Raw proof certificate](../../evidence/claim5/raw_proof.json)
- [Independent checker output](../../evidence/claim5/independent_checker_output.json)
- [Negative-control output](../../evidence/claim5/negative_control_output.json)
- [Executable source](../../evidence/claim5/claim5_attention.py)
- [Method](../../evidence/claim5/method.md)
- [Limitations](../../evidence/claim5/limitations.md)

## Claim 3 — VERIFIED

**Exact source statement.** Under bounded task functions, common `P_X`, and the
displayed conditional drift/MGF assumptions for every wrong task, Theorem 3
states for every `k>=1` that mixture posterior variance is at most true-family
minimax risk plus

`5 B_f^2[((1-alpha_i*)/alpha_i*)e^(-D_min k/2)+(T-1)e^(-Ck)]`,

where `C=min_j D_j^2/[8(nu_j^2+b_j D_j/2)]`.

**Universal proof certificate.** Common `P_X` cancels in the predictive
likelihood ratio. Iterating the conditional MGF and selecting
`lambda=D/[2(nu^2+bD/2)]` gives a valid Chernoff parameter
(`b*lambda<=1`) and an exponent at least the displayed `C`. Posterior odds
satisfy `1-pi_i=S/(1+S)<=S`. Total variance over task type adds at most
`(1+4)B_f^2` per unit wrong posterior mass. Finally, minimax risk dominates
prior-average risk, whose pointwise optimum is the posterior mean. These steps
are symbolic in every `k>=1`; no finite task family supplies the quantifier.

**Independent checker.** Exact arithmetic completed **4,568 exact rational checks**:
216 concentration-rate parameter cases, 3,402 mixture-variance
cases, 575 posterior-odds cases, and 375 Bayes/minimax cases.

**Negative controls.** Replacing coefficient 5 by 3 fails on a bounded
two-task mixture by exact residual `1/16`. Setting `D_j=0` is rejected at the
assumptions gate rather than misreported as a counterexample.

**Downloadable evidence.**

- [Claim contract](../../evidence/claim3/claim_contract.json)
- [Raw proof certificate](../../evidence/claim3/raw_proof.json)
- [Independent checker output](../../evidence/claim3/independent_checker_output.json)
- [Negative-control output](../../evidence/claim3/negative_control_output.json)
- [Executable source](../../evidence/claim3/claim3_concentration.py)
- [Method](../../evidence/claim3/method.md)
- [Limitations](../../evidence/claim3/limitations.md)

## Claim 4 — VERIFIED

**Exact source statement.** For every parameter `theta`, Theorem 4 bounds the
absolute source-to-target change in Bayes Gap by

`[2(B_M+B_f)/p] sum_k (L+Lambda_alpha) W_alpha^(k)`,

with
`Lambda_alpha=(L_s Lip(phi_theta)+L_c)(diam(U)+diam(C))^(1-alpha)`.

**Universal proof certificate.** Mean pooling plus the encoder/decoder
Lipschitz constants and `t<=D^(1-alpha)t^alpha` give `Lambda_alpha`; the
assumed Bayes modulus contributes `L`. The identity
`|a^2-b^2|=|a-b||a+b|` gives the exact `2(B_M+B_f)` factor. Under every
source-target coupling, expectation difference is bounded by the Lipschitz
modulus times expected prompt distance. Taking the infimum over couplings and
averaging over `k` is exactly the displayed Wasserstein bound.

**Independent checker.** **4,058 exact rational cases** passed: 1,600
architectural-modulus, 44 Hölder conversion, 164 squared-loss, and 2,250
two-point transport cases.

**Negative controls and interpretation.** Removing the factor 2 fails by exact
residual `1`. More importantly, Theorem 4 does **not** assert posterior
variance invariance across domains. With prior one-half on bounded noiseless
tasks `f_+(x)=x`, `f_-(x)=-x`, source `P_X=delta_0`, and target `Q_X` uniform
on `{0,1}`, the one-context posterior variance is source `0`, target `1/4`.
Thus “intrinsic to the target” means model-independent within the fixed target
domain, not invariant under input shift.

**Downloadable evidence.**

- [Claim contract](../../evidence/claim4/claim_contract.json)
- [Raw proof certificate](../../evidence/claim4/raw_proof.json)
- [Independent checker output](../../evidence/claim4/independent_checker_output.json)
- [Negative-control output](../../evidence/claim4/negative_control_output.json)
- [Executable source](../../evidence/claim4/claim4_stability.py)
- [Method](../../evidence/claim4/method.md)
- [Limitations](../../evidence/claim4/limitations.md)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
| 2 | this page | yes | yes | yes | yes | yes | yes | FALSIFIED |
| 3 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
| 4 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
| 5 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |

## Historical rejected baseline

The [old verification run](#/verification-run) is preserved for history but is
not the current verifier. It used an unavailable `core.py` and all five of its
claims were judged `toy`.
