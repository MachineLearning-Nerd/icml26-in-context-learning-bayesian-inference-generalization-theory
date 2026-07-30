---
title: "Repro - ICL Bayesian Risk Decomposition"
emoji: 🎯
colorFrom: yellow
colorTo: red
sdk: static
pinned: false
tags:
 - trackio
 - trackio-logbook
 - open-experiment
 - icml2026-repro
 - paper-BUFSSOuphA
---

# Current verification first

The current campaign supersedes the toy verifier in judged revision
`b604006ac298769e9dcee6ecb42b45369eb68cce`.

- [Current claim-by-claim verification](#/current)
- [Claim 2 exact counterexample](evidence/claim2/raw_counterexample.json)
- [Cumulative executable verifier](repro/src/verify.py)
- [Pinned environment](pyproject.toml) and [lockfile](uv.lock)
- [Immutable judged README snapshot](historical/judged_b604006a/README.md)
- [Immutable judged logbook snapshot](historical/judged_b604006a/logbook.json)

The old pages remain reachable below and are labeled **Historical rejected
baseline**. Current exact results: Claims 1, 3, 4, and 5 `VERIFIED`; Claim 2
`FALSIFIED`.

# Repro - ICL Bayesian Risk Decomposition

An open experiment logbook, published with [Trackio](https://github.com/gradio-app/trackio).
