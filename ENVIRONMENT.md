# Environment and reproduction contract

## Fixed command

```bash
uv sync --locked
uv run --locked python repro/src/verify.py
```

The formal campaign uses Python `3.12`, the repository-level locked
environment, one local CPU process, no GPU, and no third-party runtime
dependency beyond the locked standard-library execution path. Scientific
verifier nodes complete in under `0.15` seconds; the final release-gate run
is recorded in the OpenResearch artifacts. External compute cost was `$0`.

The tutorial uses the same lockfile:

```bash
uv run --locked marimo edit notebooks/icl_bayesian_reproduction.py
uv run --locked marimo run notebooks/icl_bayesian_reproduction.py
```

The cumulative verifier is the reproducibility entrypoint. This cleanup
records and verifies the existing evidence bundle; it does not silently
replace it with an untracked rerun.

