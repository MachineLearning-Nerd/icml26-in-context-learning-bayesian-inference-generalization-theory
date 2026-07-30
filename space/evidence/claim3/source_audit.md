# Claim 3 source audit

- Source: `https://ar5iv.labs.arxiv.org/html/2510.10981`
- Retrieved: 2026-07-30 with an explicit browser User-Agent
- SHA-256: `6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`
- Statement anchor: `Thmtheorem3`
- Supporting anchors: `Thmassumption1`, Equation (15), Equations (16)–(18), and Lemma 3 in Appendix G

The theorem assumes bounded task functions, a common input distribution, a
strictly positive per-step information gap for every wrong type, and the
displayed conditional MGF bound throughout `|lambda|<=1/b_j`. It quantifies
over every integer `k>=1`.

The exact claimed rate is
`C=min_j D_j^2/[8(nu_j^2+b_j D_j/2)]`. The conclusion is an upper bound on
expected mixture posterior variance, not an equality or a fitted empirical
decay rate. Its first term is the true task family's minimax prediction risk;
the task-identification remainder has coefficient `5 B_f^2`.
