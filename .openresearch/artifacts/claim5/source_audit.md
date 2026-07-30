# Claim 5 source audit

Source HTML SHA-256:
`6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`.
Anchor: `Thmdefinition2`.

Definition 2 specifies a ReLU feature encoder `phi_theta: U -> Delta^(m-1)`,
the context aggregation `k^{-1} sum_i phi_theta(x_i,y_i)`, and a clipped ReLU
decoder that also receives the query. The preceding paragraph identifies this
as uniform attention with `Q=K=0`.

For any context length `k>=1`, scaled dot-product attention has all-zero scores.
Softmax therefore assigns exact weight `1/k` to every value vector. Setting
`V_i=phi_theta(x_i,y_i)` gives the displayed Definition 2 expression exactly.
