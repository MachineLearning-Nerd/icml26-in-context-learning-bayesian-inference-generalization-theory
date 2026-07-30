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

The second review is performed from a fresh export of the final candidate
commit. Its exact commit, complete opened-file trace, and conclusion are
recorded before the formal release-gate run.
