#!/usr/bin/env python3
"""Verify the public documentation, branch namespace, and commit identity."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPOSITORY = "MachineLearning-Nerd/icml26-in-context-learning-bayesian-inference-generalization-theory"
CANONICAL = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
REQUIRED_FILES = {
    "README.md",
    "branch-audit.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "REPORT.md",
    "CITATION.cff",
    "AUTHOR_THANK_YOU.md",
    "STATUS.md",
    "claims.json",
    "reproduction_verdicts.json",
    "AUTONOMOUS_STATE.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def main() -> None:
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    assert not missing, f"missing required files: {missing}"
    assert not git("status", "--porcelain"), "working tree is not clean"
    assert not git("for-each-ref", "--format=%(refname)", "refs/original"), "refs/original remains"

    remote = git("remote", "get-url", "origin").removesuffix(".git")
    assert remote.endswith(REPOSITORY), remote

    branch_lines = git("ls-remote", "--heads", "origin").splitlines()
    remote_branches = {
        line.split("\t", 1)[1].removeprefix("refs/heads/")
        for line in branch_lines
        if "\t" in line
    }
    assert remote_branches == {
        "main",
        "audit/claim-1-risk-identity",
        "audit/claim-2-cardinality-collision",
        "audit/claim-3-posterior-concentration",
        "audit/claim-4-wasserstein-stability",
        "audit/claim-5-uniform-attention",
        "audit/protected-judged-baseline",
        "release/evaluator-visible-candidate",
        "release/final-gates-red-team",
    }, remote_branches

    default_head = git("symbolic-ref", "--short", "refs/remotes/origin/HEAD")
    assert default_head == "origin/main", default_head

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    assert identities == {f"{CANONICAL} | {CANONICAL}"}, identities
    assert "Co-authored-by:" not in git("log", "--all", "--format=%B"), "co-author trailer found"

    claims = json.loads((ROOT / "claims.json").read_text())
    assert claims["overall_status"] == "PARTIAL_CLAIMS_1_3_4_5_VERIFIED_CLAIM_2_THEOREM_2_FALSIFIED"
    assert [claim["id"] for claim in claims["claims"]] == ["C1", "C2", "C3", "C4", "C5"]

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(remote_branches)} commits={git('rev-list', '--all', '--count')} "
        "claims=C1_verified,C2_theorem2_falsified,C3:C5_verified "
        "historical_score=5/10 current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()

