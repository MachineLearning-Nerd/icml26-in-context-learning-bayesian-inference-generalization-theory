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

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
| 2 | pending | no | no | no | no | no | no | TOY |
| 3 | pending | no | no | no | no | no | no | TOY |
| 4 | pending | no | no | no | no | no | no | TOY |
| 5 | pending | no | no | no | no | no | no | TOY |

## Historical rejected baseline

The [old verification run](#/verification-run) is preserved for history but is
not the current verifier. It used an unavailable `core.py` and all five of its
claims were judged `toy`.
