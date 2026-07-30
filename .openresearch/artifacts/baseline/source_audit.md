# Source audit

- Paper: *In-Context Learning Is Provably Bayesian Inference: A Generalization Theory for Meta-Learning*
- arXiv: `2510.10981`
- Retrieved: `2026-07-30` (Asia/Kolkata)
- URL: `https://ar5iv.labs.arxiv.org/html/2510.10981`
- User-Agent: `Mozilla/5.0 (compatible; OpenResearchReproduction/1.0; +https://github.com/MachineLearning-Nerd)`
- SHA-256: `6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`
- Source anchors: `Thmdefinition1`, `Thmdefinition2`, `Thmassumption1`, `Thmassumption2`, `Thmtheorem1`, `Thmtheorem2`, `Thmtheorem3`, `Thmtheorem4`

Theorem 1 quantifies over every measurable bounded map under Definition 1 and
Assumption 1. Theorem 2 assumes Definitions 1–2, Assumptions 1–2, the stated
Hölder condition for every `k=1,…,p`, ERM training on `N` prompts, and `p≥2`.
Theorem 3 assumes bounded tasks plus positive predictive divergence and a
conditional Bernstein MGF condition for every wrong task and every `t≥1`; its
bound holds for every `k≥1`. Theorem 4 assumes Definitions 1–2, Assumptions
1–2, the Theorem 2 Hölder condition, and holds for every parameter `θ`.

Definition 2 is the exact mean-pooling architecture
`Mθ(Pᵏ)=ρθ(k⁻¹Σᵢ φθ(xᵢ,yᵢ),xₖ₊₁)`, with a ReLU feature encoder followed by
`Renormτ`, a clipped ReLU decoder, spectral-product bounds, and decoder
Lipschitz bounds.
