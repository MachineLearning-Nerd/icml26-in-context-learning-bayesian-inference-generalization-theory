# Limitations and deviations

The verdict falsifies Theorem 2 exactly as written. It does not claim that a
cardinality-aware architecture, a sum-pooling architecture, or a theorem for
one fixed context length is false. Passing `k` to the decoder removes this
counterexample.

The argument is asymptotic because the theorem hides its multiplicative
constant and logarithmic exponent. It does not guess those values: a positive
lower bound versus a RHS converging to zero contradicts every fixed finite
choice of them.

The finite support includes zero-probability prompt sequences. The required
Hölder Bayes version exists there by a permutation-symmetrized Lipschitz
extension; the exact checker audits all positive-probability pairs on which
the conditional expectation is determined.
