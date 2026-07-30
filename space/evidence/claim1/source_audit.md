# Claim 1 source audit

Source: ar5iv HTML SHA-256
`6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`,
anchor `Thmtheorem1`.

The theorem assumes the prompt-generating process in Definition 1 and bounded
tasks (Assumption 1). It quantifies over a measurable bounded map `M`. For each
partial prompt `P^k`, the Bayes predictor is the conditional mean of
`f(x_{k+1})`. Both sides are averaged over `k=1,…,p`.

The proof obligation is therefore the conditional squared-loss identity for an
arbitrary integrable conditional law, followed by the finite average. Boundedness
ensures every expectation used below exists.
