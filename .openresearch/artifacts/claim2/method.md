# Method

For the observation `y=1`, the likelihood under `f_+` is `1/2` and under
`f_-` is `1/4`. Thus:

- `Pr(y_1=1)=3/8` and `E[f|y_1=1]=1/3`;
- `Pr(y_1=y_2=1)=5/32` and `E[f|y_1=y_2=1]=3/5`.

For every feature map and every `m`,
`phi(0,1)=[phi(0,1)+phi(0,1)]/2`. Since the query is also zero, every
Definition 2 model must use one shared prediction `v` on both events. Their
contribution to the average Bayes Gap is at least

`(1/2) min_v [(3/8)(v-1/3)^2+(5/32)(v-3/5)^2] = 1/255`.

This holds pointwise for every parameter, hence for every realized ERM and
after expectation over training data.

With fixed `p=2`, `d_eff=2`, `alpha=1`, choose integer
`m_N=ceil(sqrt(N))`. For every fixed polylog exponent `r`,
`m_N^-1`, `m_N log^r(2N)/(2N)`, and `log^r(2N)/N` all tend to zero.
Multiplication by any fixed implicit constant does not change the limit, so
the claimed upper bound eventually falls below the uniform lower bound.
