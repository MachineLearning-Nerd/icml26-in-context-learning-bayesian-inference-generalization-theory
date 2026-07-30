# Claim 4 source audit

- Source: `https://ar5iv.labs.arxiv.org/html/2510.10981`
- Retrieved: 2026-07-30 with an explicit browser User-Agent
- SHA-256: `6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`
- Main statement: `Thmtheorem4`
- Detailed restatement/proof: `Thmtheorem7`, Appendix C
- Assumptions: `Thmassumption1`, `Thmassumption2`

The prompt ground metric is
`dbar_k,alpha=(1/k)sum_i ||u_i-u_i'||^alpha+||c-c'||^alpha`.
The prompt Wasserstein quantity is ordinary `W_1` with this ground metric.

The theorem quantifies over every model parameter and bounds only the change in
Bayes Gap. The prose statement that posterior variance is intrinsic to the
target domain does not assert equality of posterior variance under source and
target input laws. Appendix C explicitly fixes the task and noise distributions
while changing the input law.
