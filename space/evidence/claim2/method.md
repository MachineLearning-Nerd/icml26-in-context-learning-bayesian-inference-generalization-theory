# Method

Observation `y=1` has likelihood `1/2` under `f=1` and `1/4` under `f=-1`.
The posterior mean is `1/3` after one copy and `3/5` after two. Both contexts
have exactly the same mean pool for every feature map and `m`. Their weighted
best shared prediction is `7/17`, giving average Bayes Gap at least `1/255`.

Along `m_N=ceil(sqrt(N))`, every term in the stated RHS tends to zero for
every fixed polylog exponent and implicit constant, contradicting the lower
bound.
