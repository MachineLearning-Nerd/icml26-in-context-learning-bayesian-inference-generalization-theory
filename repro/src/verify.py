"""Fixed entrypoint for the cumulative reproduction campaign."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import time
from pathlib import Path

from claim1_proof import build_certificate
from claim2_counterexample import build_certificate as build_claim2_certificate
from claim2_independent import independent_certificate as check_claim2_independently
from claim3_concentration import build_certificate as build_claim3_certificate
from claim4_stability import build_certificate as build_claim4_certificate
from claim5_attention import build_certificate as build_claim5_certificate


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
    corrected_manifest_lines = (
        ARTIFACTS / "protected_space_manifest_corrected.sha256"
    ).read_text().splitlines()
    protected_manifest = {
        line.split()[1]: line.split()[0] for line in corrected_manifest_lines
    }
    historical_pages = [
        path for path in protected_manifest if path.startswith("pages/")
    ]
    historical_snapshot = (
        ROOT / "space" / "historical" / "judged_b604006a"
    )

    return {
        "space_id_exact": verdict["space_id"] == "DineshAI/BUFSSOuphA",
        "space_revision_exact": verdict["sha"] == EXPECTED_SPACE_REVISION,
        "judge_score_exact": verdict["score"] == EXPECTED_JUDGE_SCORE,
        "five_claims_present": len(verdict["claims"]) == 5,
        "all_historical_claims_toy": all(claim["verdict"] == "toy" for claim in verdict["claims"]),
        "paper_hash_recorded": verdict["paper_source_sha256"] == EXPECTED_PAPER_SHA256,
        "protected_manifest_complete": len(manifest_lines) == 17,
        "protected_file_set_is_subset": all(
            (ROOT / "space" / path).is_file() for path in protected_manifest
        ),
        "historical_pages_unchanged": all(
            sha256(ROOT / "space" / path) == protected_manifest[path]
            for path in historical_pages
        ),
        "judged_root_snapshot_preserved": (
            sha256(historical_snapshot / "README.md")
            == protected_manifest["README.md"]
            and sha256(historical_snapshot / "logbook.json")
            == protected_manifest["logbook.json"]
        ),
        "verdict_snapshot_hash": sha256(verdict_path)
        == "485bd5f6abf2423da5ad4010a5fd0b1d861b6ef5a639cd193b6b7e9f046b3e48",
    }


def main() -> int:
    started = time.monotonic()
    checks = baseline_checks()
    claim1 = build_certificate()
    claim2 = build_claim2_certificate()
    claim2_independent = check_claim2_independently()
    claim3 = build_claim3_certificate()
    claim4 = build_claim4_certificate()
    claim5 = build_claim5_certificate()
    current_page = ROOT / "space" / "pages" / "current" / "page.md"
    visible_files = [
        ROOT / "space" / "evidence" / "claim1" / "claim_contract.json",
        ROOT / "space" / "evidence" / "claim1" / "raw_proof.json",
        ROOT / "space" / "evidence" / "claim1" / "independent_checker_output.json",
        ROOT / "space" / "evidence" / "claim1" / "negative_control_output.json",
        ROOT / "space" / "evidence" / "claim1" / "claim1_proof.py",
    ]
    claim5_visible_files = [
        ROOT / "space" / "evidence" / "claim5" / "claim_contract.json",
        ROOT / "space" / "evidence" / "claim5" / "raw_proof.json",
        ROOT / "space" / "evidence" / "claim5" / "independent_checker_output.json",
        ROOT / "space" / "evidence" / "claim5" / "negative_control_output.json",
        ROOT / "space" / "evidence" / "claim5" / "claim5_attention.py",
    ]
    claim3_visible_files = [
        ROOT / "space" / "evidence" / "claim3" / "claim_contract.json",
        ROOT / "space" / "evidence" / "claim3" / "raw_proof.json",
        ROOT / "space" / "evidence" / "claim3" / "independent_checker_output.json",
        ROOT / "space" / "evidence" / "claim3" / "negative_control_output.json",
        ROOT / "space" / "evidence" / "claim3" / "claim3_concentration.py",
    ]
    claim4_visible_files = [
        ROOT / "space" / "evidence" / "claim4" / "claim_contract.json",
        ROOT / "space" / "evidence" / "claim4" / "raw_proof.json",
        ROOT / "space" / "evidence" / "claim4" / "independent_checker_output.json",
        ROOT / "space" / "evidence" / "claim4" / "negative_control_output.json",
        ROOT / "space" / "evidence" / "claim4" / "claim4_stability.py",
    ]
    claim2_visible_files = [
        ROOT / "space" / "evidence" / "claim2" / "claim_contract.json",
        ROOT / "space" / "evidence" / "claim2" / "raw_counterexample.json",
        ROOT / "space" / "evidence" / "claim2" / "independent_checker_output.json",
        ROOT / "space" / "evidence" / "claim2" / "negative_control_output.json",
        ROOT / "space" / "evidence" / "claim2" / "claim2_counterexample.py",
        ROOT / "space" / "evidence" / "claim2" / "claim2_independent.py",
    ]
    visibility_checks = {
        "canonical_current_page": current_page.is_file(),
        "claim1_evidence_files": all(path.is_file() for path in visible_files),
        "claim1_result_inline": current_page.is_file()
        and "3,350 exact" in current_page.read_text(),
        "historical_verifier_labeled": current_page.is_file()
        and "Historical rejected baseline" in current_page.read_text(),
        "claim5_evidence_files": all(path.is_file() for path in claim5_visible_files),
        "claim5_result_inline": current_page.is_file()
        and "873 exact context permutations" in current_page.read_text(),
        "claim3_evidence_files": all(path.is_file() for path in claim3_visible_files),
        "claim3_result_inline": current_page.is_file()
        and "4,568 exact rational checks" in current_page.read_text(),
        "claim4_evidence_files": all(path.is_file() for path in claim4_visible_files),
        "claim4_result_inline": current_page.is_file()
        and "exact rational cases" in current_page.read_text()
        and "target `1/4`" in current_page.read_text(),
        "claim2_evidence_files": all(path.is_file() for path in claim2_visible_files),
        "claim2_result_inline": current_page.is_file()
        and "uniform lower bound `1/255`" in current_page.read_text()
        and "Bayes means `1/3` and `3/5`" in current_page.read_text(),
        "self_contained_space_verifier": all(
            path.is_file()
            for path in (
                ROOT / "space" / "repro" / "src" / "verify.py",
                ROOT / "space" / "pyproject.toml",
                ROOT / "space" / "uv.lock",
            )
        ),
        "illustrated_report_complete": all(
            path.is_file()
            for path in (
                ROOT / "reports" / "reproduction" / "report.md",
                ROOT / "reports" / "reproduction" / "images" / "headline-results.svg",
                ROOT / "reports" / "reproduction" / "images" / "cardinality-collision.svg",
                ROOT / "reports" / "reproduction" / "images" / "theorem3-proof-chain.svg",
                ROOT / "reports" / "reproduction" / "images" / "theorem4-shift.svg",
                ROOT / "reports" / "reproduction" / "release_report.md",
            )
        ),
        "tutorial_notebook_visible": (
            ROOT / "notebooks" / "icl_bayesian_reproduction.py"
        ).is_file(),
        "readme_current": (
            "Theorem 2 is **FALSIFIED**" in (ROOT / "README.md").read_text()
            and "Open in molab" in (ROOT / "README.md").read_text()
        ),
    }
    passed = (
        all(checks.values())
        and claim1["passed"]
        and claim2["passed"]
        and claim2_independent["passed"]
        and claim3["passed"]
        and claim4["passed"]
        and claim5["passed"]
        and all(visibility_checks.values())
    )
    result = {
        "campaign_stage": "evaluator_visible_release_candidate",
        "status": "VERIFIED" if passed else "BLOCKED",
        "passed_manifest_checks": passed,
        "checks": checks,
        "visibility_checks": visibility_checks,
        "claims": [
            {"claim": 1, "verdict": "VERIFIED" if claim1["passed"] else "BLOCKED"},
            {"claim": 2, "verdict": "FALSIFIED" if claim2["passed"] else "BLOCKED"},
            {"claim": 3, "verdict": "VERIFIED" if claim3["passed"] else "BLOCKED"},
            {"claim": 4, "verdict": "VERIFIED" if claim4["passed"] else "BLOCKED"},
            {"claim": 5, "verdict": "VERIFIED" if claim5["passed"] else "BLOCKED"},
        ],
        "claim_1_certificate": claim1,
        "claim_2_certificate": claim2,
        "claim_2_independent_checker": claim2_independent,
        "claim_3_certificate": claim3,
        "claim_4_certificate": claim4,
        "claim_5_certificate": claim5,
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
