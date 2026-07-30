"""Fixed entrypoint for the cumulative reproduction campaign."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import time
from pathlib import Path

from claim1_proof import build_certificate


ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = ROOT / ".openresearch" / "artifacts" / "baseline"
EXPECTED_PAPER_SHA256 = "6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1"
EXPECTED_SPACE_REVISION = "b604006ac298769e9dcee6ecb42b45369eb68cce"
EXPECTED_JUDGE_SCORE = 5


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def baseline_checks() -> dict[str, bool]:
    verdict_path = ARTIFACTS / "live_verdict.json"
    verdict = json.loads(verdict_path.read_text())
    manifest_lines = (ARTIFACTS / "protected_space_manifest.sha256").read_text().splitlines()

    return {
        "space_id_exact": verdict["space_id"] == "DineshAI/BUFSSOuphA",
        "space_revision_exact": verdict["sha"] == EXPECTED_SPACE_REVISION,
        "judge_score_exact": verdict["score"] == EXPECTED_JUDGE_SCORE,
        "five_claims_present": len(verdict["claims"]) == 5,
        "all_historical_claims_toy": all(claim["verdict"] == "toy" for claim in verdict["claims"]),
        "paper_hash_recorded": verdict["paper_source_sha256"] == EXPECTED_PAPER_SHA256,
        "protected_manifest_complete": len(manifest_lines) == 17,
        "verdict_snapshot_hash": sha256(verdict_path)
        == "485bd5f6abf2423da5ad4010a5fd0b1d861b6ef5a639cd193b6b7e9f046b3e48",
    }


def main() -> int:
    started = time.monotonic()
    checks = baseline_checks()
    claim1 = build_certificate()
    current_page = ROOT / "space" / "pages" / "current" / "page.md"
    visible_files = [
        ROOT / "space" / "evidence" / "claim1" / "claim_contract.json",
        ROOT / "space" / "evidence" / "claim1" / "raw_proof.json",
        ROOT / "space" / "evidence" / "claim1" / "independent_checker_output.json",
        ROOT / "space" / "evidence" / "claim1" / "negative_control_output.json",
        ROOT / "space" / "evidence" / "claim1" / "claim1_proof.py",
    ]
    visibility_checks = {
        "canonical_current_page": current_page.is_file(),
        "claim1_evidence_files": all(path.is_file() for path in visible_files),
        "claim1_result_inline": current_page.is_file()
        and "3,350 exact" in current_page.read_text(),
        "historical_verifier_labeled": current_page.is_file()
        and "Historical rejected baseline" in current_page.read_text(),
    }
    passed = all(checks.values()) and claim1["passed"] and all(visibility_checks.values())
    result = {
        "campaign_stage": "claim_1_exact_risk_identity",
        "status": "VERIFIED" if passed else "BLOCKED",
        "passed_manifest_checks": passed,
        "checks": checks,
        "visibility_checks": visibility_checks,
        "claims": [
            {"claim": 1, "verdict": "VERIFIED" if claim1["passed"] else "BLOCKED"},
            *[{"claim": index, "verdict": "TOY"} for index in range(2, 6)],
        ],
        "claim_1_certificate": claim1,
        "historical_limitation": (
            "The judged Space embeds verify.py but omits its imported core.py, so the numerical "
            "baseline cannot be independently regenerated from the protected revision."
        ),
        "compute": {
            "backend": "local",
            "estimated_cores": 1,
            "selected_flavor": "local CPU",
            "available_logical_cpus": os.cpu_count(),
            "process_threads": 1,
            "platform": platform.platform(),
            "runtime_seconds": round(time.monotonic() - started, 6),
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
