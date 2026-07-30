# Exact command and environment

```bash
uv run --locked python repro/src/verify.py
```

- Repository-level `.venv`, Python `3.12.*`, `uv.lock`
- No third-party dependencies
- Deterministic; no seeds
- Estimate: one CPU core, under one minute
- Selected compute: local CPU
- Process threads: one
