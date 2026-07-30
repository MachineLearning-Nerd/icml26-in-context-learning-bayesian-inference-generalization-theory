# Exact command and environment

```bash
uv run --locked python repro/src/verify.py
```

- Environment: repository-level `.venv`, Python `3.12.*`
- Lock: `uv.lock`
- Third-party dependencies: none
- Seeds: none; all checks are deterministic
- Estimate: one CPU core, under one minute
- Selected compute: local CPU under the authorized short-task rule
- Process threads: one
