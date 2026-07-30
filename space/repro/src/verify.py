"""Evaluator-runnable cumulative verifier packaged in the Space."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = [
    "evidence/claim1/claim1_proof.py",
    "evidence/claim2/claim2_counterexample.py",
    "evidence/claim2/claim2_independent.py",
    "evidence/claim3/claim3_concentration.py",
    "evidence/claim4/claim4_stability.py",
    "evidence/claim5/claim5_attention.py",
]


def main() -> int:
    started = time.monotonic()
    runs = {}
    passed = True
    for relative_path in SCRIPTS:
        completed = subprocess.run(
            [sys.executable, str(ROOT / relative_path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        runs[relative_path] = {
            "exit_code": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }
        passed = passed and completed.returncode == 0

    current_page = (ROOT / "pages/current/page.md").read_text()
    visibility = {
        "claim1_verified": "Claim 1 — VERIFIED" in current_page,
        "claim2_falsified": "Claim 2 — FALSIFIED" in current_page,
        "claim3_verified": "Claim 3 — VERIFIED" in current_page,
        "claim4_verified": "Claim 4 — VERIFIED" in current_page,
        "claim5_verified": "Claim 5 — VERIFIED" in current_page,
        "historical_rejected_label": "Historical rejected baseline" in current_page,
    }
    passed = passed and all(visibility.values())
    result = {
        "status": "PASS" if passed else "FAIL",
        "claims": {
            "1": "VERIFIED",
            "2": "FALSIFIED",
            "3": "VERIFIED",
            "4": "VERIFIED",
            "5": "VERIFIED",
        },
        "runs": runs,
        "visibility": visibility,
        "runtime_seconds": round(time.monotonic() - started, 6),
        "process_threads": 1,
        "seeds": [],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
