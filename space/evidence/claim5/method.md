# Method

The verifier implements the actual attention data path: dot-product scores,
softmax exponentials, normalization, and weighted value aggregation. Because
`Q=K=0`, every score is zero, `exp(0)=1`, and exact `Fraction` arithmetic
produces weights `1/k`.

It compares attention output with a separately implemented direct mean for all
873 permutations of fixed two-dimensional rational feature sequences at
lengths one through six.

The negative control changes the score vector to `[0,1]`. A 50-digit Decimal
softmax gives unequal weights, so the control must be rejected as uniform
attention.
