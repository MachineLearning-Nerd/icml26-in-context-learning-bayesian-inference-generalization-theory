# Method

The primary checker expands squared loss around the exact conditional mean:

`(M-F)^2 - (M-mu)^2 - (F-mu)^2 = 2(M-mu)(mu-F)`.

Conditioning on the prompt makes `M` and `mu` fixed, while
`E[mu-F | prompt]=0`. The residual therefore vanishes exactly, not
approximately. Averaging the identity over prompt draws and `k=1,…,p` yields
the theorem.

An independent checker uses `fractions.Fraction` and exhaustively enumerates
finite conditional distributions with one to three support points, rational
positive weights with denominator at most four, values and predictions in
`{-2,-1,0,1,2}`. It uses a separately evaluated moment formula and requires
bit-exact equality.

The negative control shifts the center by `1/2` and intentionally omits the
resulting cross term. Its exact residual must be nonzero.
