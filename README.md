# In-Context Learning Is Provably Bayesian Inference — independent reproduction

[![Open in Molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-in-context-learning-bayesian-inference-generalization-theory/blob/main/notebooks/icl_bayesian_reproduction.py)

Independent reproduction and claim audit for **In-Context Learning Is
Provably Bayesian Inference: A Generalization Theory for Meta-Learning** by
Tomoya Wakayama and Taiji Suzuki.

- Paper: [arXiv:2510.10981](https://arxiv.org/abs/2510.10981)
- Clean repository: [MachineLearning-Nerd/icml26-in-context-learning-bayesian-inference-generalization-theory](https://github.com/MachineLearning-Nerd/icml26-in-context-learning-bayesian-inference-generalization-theory)
- Evaluator-visible candidate: [`space/pages/current`](space/pages/current/page.md)
- Reproduction command: `uv run --locked python repro/src/verify.py`

## What the paper does

The paper develops a finite-sample meta-learning theory for in-context
learning. It decomposes prediction risk into Bayes Gap and Posterior Variance,
analyzes uniform-attention Transformers as mean-pooled feature models, and
studies task identification, distribution shift, and the convergence of
in-context predictions toward Bayesian inference.

## Reproduction status

The release replaces the historical Gaussian proxy checks with exact claim
contracts. Four claims are verified by universal proof or architecture
certificates. Theorem 2 (the Bayes Gap rate) is falsified as written by an
assumption-satisfying representation collision.

Overall status: `PARTIAL_CLAIMS_1_3_4_5_VERIFIED_CLAIM_2_THEOREM_2_FALSIFIED`.
This is a scoped audit of the shared mean-pooled architecture and the exact
paper statements. A cardinality-aware or sum-pooling decoder is outside the
falsified scope. `publication_allowed=false`, `score_claim=false`, and
`official_author_endorsement=false` until an independent evaluator judges the
public revision.

| Release result | Meaning |
| --- | --- |
| Claims 1, 3, 4, and 5: **VERIFIED** | Exact symbolic or architectural certificates pass their independent checkers and controls. |
| Claim 2 / Theorem 2: **FALSIFIED** | Mean pooling cannot distinguish one copy from two copies of the same observation, but their Bayesian posterior means differ. |
| Blocked claims: none | Every contract has a terminal verdict. |
| Historical live judge: `5/10` | This remains the recorded score. |
| Projected `9–10/10`: forecast only | A new score requires live evaluation of the published revision. |

The source audit used the arXiv HTML retrieved on 2026-07-30 with SHA-256
`6173e746b37f95c44a391974f88c622e8ae77a3d1ca792bdfffb09f5c85a2aa1`. The
current arXiv page is linked above; the claim artifacts preserve the exact
source hash used for the audit.

## Claim-to-evidence map

The fixed entrypoint is [`repro/src/verify.py`](repro/src/verify.py). It
loads one independent module per claim, runs baseline/release visibility
checks, emits a machine-readable result, and exits nonzero if any proof,
counterexample, control, or release gate fails. Durable artifacts are under
[`.openresearch/artifacts`](.openresearch/artifacts), with evaluator-facing
copies under [`space/evidence`](space/evidence).

| Claim | Paper statement | How the result is produced | Verdict |
| --- | --- | --- | --- |
| 1. Risk decomposition | `R(M)=R_BG(M)+R_PV` for every bounded measurable predictor and every prompt length. | [`claim1_proof.py`](repro/src/claim1_proof.py) expands squared loss around the conditional mean, cancels the cross term by conditional expectation, and averages over `k=1,…,p`. An exact `Fraction` checker covers 3,350 cases; a wrong-center control leaves residual `-3/2`. | **VERIFIED** |
| 2. Bayes Gap rate | Theorem 2 claims the ERM Bayes Gap tends to zero at its displayed `m,N,p` rate for a shared mean-pooled decoder. | [`claim2_counterexample.py`](repro/src/claim2_counterexample.py) fixes `p=2`, task functions `f_±(x)=±1`, `x=0`, and noise `Pr(-2,0,2)=(1/4,1/2,1/4)`. One and two identical observations have the same mean pool for every encoder and feature count, but Bayes means `1/3` and `3/5`; exact optimization gives `R_BG≥1/255` for every model. With `m_N=ceil(sqrt(N))`, the claimed RHS tends to zero. | **FALSIFIED** |
| 3. Posterior concentration | Theorem 3 bounds mixture posterior variance by the true-family minimax risk plus an exponential task-identification remainder. | [`claim3_concentration.py`](repro/src/claim3_concentration.py) reconstructs the likelihood-ratio chain, conditional MGF/Chernoff rate `C`, posterior odds, total variance, and Bayes-to-minimax comparison. Four exact checkers cover 4,568 rational cases; a weakened coefficient and `D_j=0` controls are rejected. | **VERIFIED** |
| 4. Wasserstein stability | Theorem 4 bounds the change in Bayes Gap under input-distribution shift using Wasserstein prompt distances and the exact architectural Hölder modulus. | [`claim4_stability.py`](repro/src/claim4_stability.py) derives the encoder/decoder modulus, the `2(B_M+B_f)` squared-loss factor, and the coupling/Wasserstein step. Exact checkers cover 4,058 cases; a factor-of-two control is rejected. A separate source/target task mixture correctly rejects the stronger claim that posterior variance is invariant. | **VERIFIED** |
| 5. Uniform attention | Definition 2's uniform-attention Transformer is exactly mean pooling when `Q=K=0`. | [`claim5_attention.py`](repro/src/claim5_attention.py) executes dot-product scores, softmax, normalization, and value aggregation with exact `Fraction` arithmetic. It checks all 873 permutations at context lengths 1–6; a nonzero-score control produces unequal weights and is rejected. | **VERIFIED** |

### Claim 2 collision, step by step

The falsification does not depend on training, a finite fit, or a chosen
neural-network width:

1. Set `p=2` and make the input always `x=0`; task functions are `+1` and
   `-1` with equal prior probability.
2. For the positive observation `y=1`, the one-example event has probability
   `3/8` and Bayesian mean `1/3`; the two-example repeated event has
   probability `5/32` and Bayesian mean `3/5`.
3. Definition 2 sends both contexts through
   `k⁻¹ Σᵢ φ(xᵢ,yᵢ)`. One copy and two identical copies therefore have exactly
   the same representation for every feature map and every `m`.
4. One shared prediction cannot equal both posterior means. Minimizing the
   weighted squared loss gives prediction `7/17` and an exact Bayes Gap lower
   bound `1/255`.
5. The theorem's claimed upper bound tends to zero along
   `m_N=ceil(sqrt(N))`, contradicting the fixed positive lower bound.

Giving the context length `k` to the decoder removes this collision and is
therefore retained as a negative control; it is not part of the falsified
architecture.

### How verdicts are produced

1. Each claim contract fixes the paper anchor, assumptions, quantifiers, and
   acceptance rule.
2. A source audit records the exact theorem interpretation and any boundary
   between the paper's prose and formal statement.
3. The claim module produces a symbolic proof, exact counterexample, or exact
   architecture identity—never a fitted slope or formula-selected sample.
4. An independent checker recomputes decisive values, and a negative control
   must be rejected. The cumulative verifier also checks the protected
   historical manifest, release allowlist, evaluator visibility, and tutorial
   links.

The historical three-family Gaussian experiment is preserved as rejected
baseline context only. It is not used to establish any current verdict.

## Branches

`main` is the publication surface. The complete historical-to-clean mapping
is documented in [branch-audit.md](branch-audit.md).

| Clean branch | Purpose |
| --- | --- |
| `audit/protected-judged-baseline` | Freeze the historical judged `5/10` toy baseline and protected Space manifest. |
| `audit/claim-1-risk-identity` | Build and check the universal squared-risk identity. |
| `audit/claim-2-cardinality-collision` | Construct and independently check the Theorem 2 falsification. |
| `audit/claim-3-posterior-concentration` | Reconstruct the universal posterior-concentration proof. |
| `audit/claim-4-wasserstein-stability` | Reconstruct the Wasserstein Bayes-Gap stability proof and interpretation control. |
| `audit/claim-5-uniform-attention` | Execute the exact `Q=K=0` scaled-dot-product attention path. |
| `release/evaluator-visible-candidate` | Assemble the evaluator-facing claim pages, evidence, and navigation. |
| `release/final-gates-red-team` | Record final release gates, red-team pass, and judge-waiting state. |

Branch names describe evidence role, not scientific confidence. Historical
`orx/` names are retained only in the branch audit.

## Repository map

| Path | Role |
| --- | --- |
| `repro/src/verify.py` | Fixed cumulative verifier and release-gate entrypoint. |
| `repro/src/claim1_proof.py` | Claim 1 symbolic risk identity. |
| `repro/src/claim2_counterexample.py` and `claim2_independent.py` | Theorem 2 collision construction and independent exact checker. |
| `repro/src/claim3_concentration.py` | Theorem 3 proof certificate. |
| `repro/src/claim4_stability.py` | Theorem 4 coupling/Wasserstein proof certificate. |
| `repro/src/claim5_attention.py` | Exact uniform-attention identity. |
| `.openresearch/artifacts/claim1..claim5` | Contracts, source audits, raw results, checkers, controls, and limitations. |
| `reports/reproduction` | Illustrated report, release report, and evaluator-blind red team. |
| `space` | Evaluator-facing pages, evidence mirror, and preserved historical baseline. |
| `notebooks/icl_bayesian_reproduction.py` | Self-contained marimo tutorial. |

## Reproduce locally

```bash
uv sync --locked
uv run --locked python repro/src/verify.py
```

The formal campaign uses Python 3.12, a repository-level locked environment,
one local CPU process, and no GPU. Scientific verifier nodes complete in under
`0.15` seconds; the final release-gate run is recorded in the OpenResearch
artifacts. External compute cost was `$0`.

For the tutorial:

```bash
uv run --locked marimo edit notebooks/icl_bayesian_reproduction.py
uv run --locked marimo run notebooks/icl_bayesian_reproduction.py
```

## Scope and limitations

- Claims 1, 3, 4, and 5 are proof or architecture certificates, not claims
  that a finite enumeration alone proves a universal theorem.
- Claim 2 falsifies the shared mean-pooled architecture's Theorem 2 as
  written. A cardinality-aware or sum-pooling decoder, or a theorem for one
  fixed context length, is outside this counterexample.
- Claim 4 verifies the Bayes-Gap shift bound; it does not assert posterior
  variance is invariant between source and target input laws.
- The historical judged score and projected score are kept separate from
  current evidence; only a live evaluator can change the score.
- This repository is an independent reproduction and is not author-endorsed.

## Citation

```bibtex
@article{wakayama2025incontext,
  title={In-Context Learning Is Provably Bayesian Inference: A Generalization Theory for Meta-Learning},
  author={Wakayama, Tomoya and Suzuki, Taiji},
  journal={arXiv preprint arXiv:2510.10981},
  year={2025},
  doi={10.48550/arXiv.2510.10981}
}
```

Machine-readable citation metadata is also available in
[`CITATION.cff`](CITATION.cff), and the author note is kept separately in
[`AUTHOR_THANK_YOU.md`](AUTHOR_THANK_YOU.md).

## Thank you

Thank you to Tomoya Wakayama and Taiji Suzuki for developing and sharing this
work. Its risk decomposition, posterior-concentration argument, Wasserstein
stability statement, and explicit uniform-attention architecture made it
possible to distinguish valid universal components from the shared-decoder
cardinality collision in Theorem 2.

Documentation, cleanup, and independent verification in this repository are
maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd).
That attribution applies to this reproduction work and does not change the
provenance of the paper or the authors' artifacts.
