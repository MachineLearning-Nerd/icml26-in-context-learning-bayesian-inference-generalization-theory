# Method

The verifier independently reconstructs the five proof obligations.

1. Chain predictive likelihood ratios; common `P_X` cancels.
2. Iterate the conditional MGF and use
   `lambda=D/[2(nu^2+bD/2)]`. Exact algebra checks both `b*lambda<=1` and
   that its exponent is at least the theorem's stated `C`.
3. Convert likelihood ratios to posterior odds and use
   `S/(1+S)<=S`, splitting on the simultaneous concentration event.
4. Apply total variance over task type. Boundedness contributes at most
   `B_f^2` to the within-type difference and `4B_f^2` to the between-type
   variance per unit wrong posterior mass.
5. Show minimax risk dominates prior-average risk, whose pointwise minimizer
   is the posterior mean.

Four exact rational checkers exercise the concentration-rate algebra, mixture
variance, posterior odds, and Bayes/minimax ordering. They are independent bug
detectors; the symbolic derivation supplies the universal quantifier.
