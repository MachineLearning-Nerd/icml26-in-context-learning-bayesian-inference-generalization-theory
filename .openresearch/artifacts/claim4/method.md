# Method

The proof is reconstructed without invoking a fitted shift experiment.

1. Mean pooling plus encoder and decoder Lipschitzness bounds model change.
   `t<=D^(1-alpha)t^alpha` converts it to the paper's prompt metric and exact
   `Lambda_alpha`.
2. The assumed Bayes-predictor modulus adds `L`.
3. Bounded outputs and `|a^2-b^2|=|a-b||a+b|` give the exact factor
   `2(B_M+B_f)`.
4. Under any source-target coupling, the expectation difference is at most
   the expected pointwise difference. Apply the Lipschitz bound and take the
   infimum over couplings, which is the stated Wasserstein distance.
5. Average the result over `k=1,...,p`.

Exact rational sweeps check each algebraic component. A separate bounded task
mixture rejects the old, stronger interpretation that posterior variance must
be invariant across the two domains.
