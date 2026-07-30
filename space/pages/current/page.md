# Current verification

This page is the canonical evaluator entrypoint. It supersedes the verifier in
the judged revision `b604006ac298769e9dcee6ecb42b45369eb68cce`.

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

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
| 2 | pending | no | no | no | no | no | no | TOY |
| 3 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
| 4 | pending | no | no | no | no | no | no | TOY |
| 5 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |

## Historical rejected baseline

The [old verification run](#/verification-run) is preserved for history but is
not the current verifier. It used an unavailable `core.py` and all five of its
claims were judged `toy`.
