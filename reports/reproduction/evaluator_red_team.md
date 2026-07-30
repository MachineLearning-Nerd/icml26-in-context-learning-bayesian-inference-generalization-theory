# Evaluator-blind pre-publication red team

The reviewer received only a fresh candidate tree and the evaluator rubric.
No internal OpenResearch paths, unpublished branches, or repository knowledge
were supplied. Navigation began at `README.md`, followed the `#/current`
route through `logbook.json`, and then followed only links on
`pages/current/page.md`.

## Round 1 — release candidate `4b74efb`

The fresh tree was exported from commit
`4b74efb6e60d7d13eb25039b8920036c57e83723`. The reviewer opened:

- `README.md`, `logbook.json`, and `pages/current/page.md`;
- `pyproject.toml`, `uv.lock`, and `repro/src/verify.py`;
- for every claim, the linked contract, raw result, independent-checker
  output, negative-control output, executable source, method, and limitations;
- Claim 2's second independent source;
- the current and historical navigation records in `logbook.json`.

The reviewer could locate the current verdict, inline numbers, raw data,
checker, control, code, fixed command, environment, historical label, and
formal provenance for all five claims. One release-blocking discoverability
gap remained: each `source_audit.md`, `exact_command.md`, and `EVAL.md` existed
in the candidate but was not linked from the canonical page. Claim 1 also
contained stale prose saying its formal metadata would be copied later.

Conclusion: **BLOCKED pending navigation fixes**. No scientific certificate
failed.

## Fix

The canonical page now links the source/assumption audit, exact command and
environment record, and evaluation record for every claim. The stale Claim 1
sentence now points to the completed provenance table. The packaged verifier
and repository verifier both require those links and files.

## Round 2

The second review used a fresh export of commit
`061d6b3f1a52f25c84adbe863c652cf69403ab1f`, whose Space subtree is
`121bacacf9b7665cd19fc49740350a12d10d9862`. It began again at `README.md`
and opened exactly:

```text
README.md
logbook.json
pages/current/page.md
pyproject.toml
uv.lock
repro/src/verify.py
evidence/claim1/EVAL.md
evidence/claim1/claim1_proof.py
evidence/claim1/claim_contract.json
evidence/claim1/exact_command.md
evidence/claim1/independent_checker_output.json
evidence/claim1/limitations.md
evidence/claim1/method.md
evidence/claim1/negative_control_output.json
evidence/claim1/raw_proof.json
evidence/claim1/source_audit.md
evidence/claim2/EVAL.md
evidence/claim2/claim2_counterexample.py
evidence/claim2/claim2_independent.py
evidence/claim2/claim_contract.json
evidence/claim2/exact_command.md
evidence/claim2/independent_checker_output.json
evidence/claim2/limitations.md
evidence/claim2/method.md
evidence/claim2/negative_control_output.json
evidence/claim2/raw_counterexample.json
evidence/claim2/source_audit.md
evidence/claim3/EVAL.md
evidence/claim3/claim3_concentration.py
evidence/claim3/claim_contract.json
evidence/claim3/exact_command.md
evidence/claim3/independent_checker_output.json
evidence/claim3/limitations.md
evidence/claim3/method.md
evidence/claim3/negative_control_output.json
evidence/claim3/raw_proof.json
evidence/claim3/source_audit.md
evidence/claim4/EVAL.md
evidence/claim4/claim4_stability.py
evidence/claim4/claim_contract.json
evidence/claim4/exact_command.md
evidence/claim4/independent_checker_output.json
evidence/claim4/limitations.md
evidence/claim4/method.md
evidence/claim4/negative_control_output.json
evidence/claim4/raw_proof.json
evidence/claim4/source_audit.md
evidence/claim5/EVAL.md
evidence/claim5/claim5_attention.py
evidence/claim5/claim_contract.json
evidence/claim5/exact_command.md
evidence/claim5/independent_checker_output.json
evidence/claim5/limitations.md
evidence/claim5/method.md
evidence/claim5/negative_control_output.json
evidence/claim5/raw_proof.json
evidence/claim5/source_audit.md
```

Every linked file existed. The packaged fixed command
`uv run --locked python repro/src/verify.py` exited zero with status `PASS`.
The reviewer located all source quantifiers, assumption audits, inline data,
raw downloads, code, checkers, controls, limitations, formal provenance, and
historical labeling without external hints.

Conclusion: **PASS — release-ready**.
