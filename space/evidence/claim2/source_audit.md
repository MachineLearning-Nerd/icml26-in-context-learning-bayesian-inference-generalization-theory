# Claim 2 source audit

- Source: `https://ar5iv.labs.arxiv.org/html/2510.10981`
- Retrieved: 2026-07-30 with explicit User-Agent
- SHA-256: `6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`
- Anchors: `Thmtheorem2`, `Thmdefinition2`, `Thmlemma5`, `Thmlemma6`

Theorem 2 uses one shared model across `k=1,...,p`, but Definition 2 gives its
decoder only a mean-pooled feature and the query—not `k`. Lemma 5 constructs
an approximation separately for every fixed `k`; its use does not establish a
single simultaneous decoder.

The counterexample has `p=2`, `d_eff=2`, `alpha=1`, one task type, constant
bounded tasks `f=±1`, input zero, and centered noise on `{-2,0,2}` with masses
`{1/4,1/2,1/4}`. Its variance is 2 and
`E exp(lambda epsilon)=cosh²(lambda)<=exp(lambda²)`.
