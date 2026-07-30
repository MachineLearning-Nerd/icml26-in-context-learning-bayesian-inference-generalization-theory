# Limitations and deviations

This verifies the theorem's stability upper bound, not its tightness for a
particular trained model. The finite checkers do not supply the universal
quantifier; the coupling derivation does.

The result requires finite architectural and support constants and an
alpha-Hölder Bayes predictor. It gives no small bound when those constants or
the prompt Wasserstein distance are large.

Posterior variance can change when the target input law changes. The theorem
only says it is independent of the selected model after the target domain is
fixed.
