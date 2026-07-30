# Exact command and environment

Fixed command inherited from the baseline:

```bash
uv run --locked python repro/src/verify.py
```

Python is pinned to `3.12.*` by `pyproject.toml` and resolved by `uv.lock`.
There are no third-party dependencies. Seed: none; the proof is deterministic.
Estimated requirement: one CPU core and under one minute.
