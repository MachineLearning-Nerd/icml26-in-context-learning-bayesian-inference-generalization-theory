# Claim 2 source audit

- Source: `https://ar5iv.labs.arxiv.org/html/2510.10981`
- Retrieved: 2026-07-30 with an explicit browser User-Agent
- SHA-256: `6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`
- Statement: `Thmtheorem2`
- Architecture: `Thmdefinition2`
- Proof dependencies: `Thmlemma5`, `Thmlemma6`

Theorem 2 trains one shared parameter `theta` over all prefix lengths
`k=1,...,p`. Definition 2 passes only
`k^{-1} sum_i phi_theta(x_i,y_i)` and the query to the decoder; it does not
pass `k`.

Lemma 5 is stated separately “for every k” and constructs a decoder for that
fixed `k`. The Theorem 2 proof applies it without establishing one decoder
that works simultaneously for all `k`. Repeating one identical example once
or twice produces exactly the same mean-pooled summary, although Bayesian
evidence generally changes with repetition.

The counterexample uses `p=2`, `d_feat=1`, `d_eff=2`, `alpha=1`, and one task
type. Its task prior is uniform on `f_+(x)=1` and `f_-(x)=-1`; `P_X` is point
mass at zero. Noise has probabilities `1/4,1/2,1/4` on `-2,0,2`.
It is centered, has variance 2, and
`E exp(lambda epsilon)=cosh(lambda)^2<=exp(lambda^2)`, matching a
sub-Gaussian proxy `sigma_epsilon^2=2`.

On the finite positive-probability prompt support, exact enumeration verifies
the Bayes predictor is 1-Lipschitz at both lengths. A permutation-symmetrized
McShane extension supplies the same Hölder version on all of the finite
domain, including zero-probability sequences.
