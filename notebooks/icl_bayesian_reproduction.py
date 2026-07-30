import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from fractions import Fraction

    return Fraction, mo


@app.cell
def _(mo):
    mo.md(r"""
    # In-context learning as Bayesian inference: exact reproduction

    | Claim | Exact outcome | Strongest evidence |
    |---|---|---|
    | 1 | **VERIFIED** | conditional risk identity |
    | 2 | **FALSIFIED** | `R_BG ≥ 1/255` for every mean-pooled model |
    | 3 | **VERIFIED** | universal concentration derivation |
    | 4 | **VERIFIED** | universal Wasserstein coupling proof |
    | 5 | **VERIFIED** | exact `Q=K=0` attention execution |

    This notebook opens with the already-produced evidence. It performs only tiny
    exact-arithmetic calculations; no training or expensive run is required.
    """)
    return


@app.cell
def _(Fraction):
    likelihood_plus = Fraction(1, 2)
    likelihood_minus = Fraction(1, 4)
    q1 = (likelihood_plus + likelihood_minus) / 2
    q2 = (likelihood_plus**2 + likelihood_minus**2) / 2
    mu1 = (likelihood_plus - likelihood_minus) / (
        likelihood_plus + likelihood_minus
    )
    mu2 = (likelihood_plus**2 - likelihood_minus**2) / (
        likelihood_plus**2 + likelihood_minus**2
    )
    shared_prediction = (q1 * mu1 + q2 * mu2) / (q1 + q2)
    lower_bound = Fraction(1, 2) * (
        q1 * (shared_prediction - mu1) ** 2
        + q2 * (shared_prediction - mu2) ** 2
    )
    return lower_bound, mu1, mu2, q1, q2, shared_prediction


@app.cell
def _(lower_bound, mo, mu1, mu2, q1, q2, shared_prediction):
    mo.md(
        f"""
        ## The decisive cardinality collision

        The fixed counterexample has a uniform prior on constant tasks
        `f(x)=±1`, input `x=0`, and centered noise on `(-2,0,2)` with masses
        `(1/4,1/2,1/4)`.

        - One `y=1`: probability `{q1}`, posterior mean `{mu1}`.
        - Two repeated `y=1`: probability `{q2}`, posterior mean `{mu2}`.
        - Both contexts map to the same mean feature for every encoder.
        - Best shared prediction: `{shared_prediction}`.
        - Exact average Bayes-Gap lower bound: **`{lower_bound}`**.

        The theorem's RHS tends to zero along `m=ceil(sqrt(N))`, while this
        lower bound applies to every model and every ERM.
        """
    )
    return


@app.cell
def _(mo):
    architecture = mo.ui.dropdown(
        options={
            "Mean pooling (paper)": "collision remains",
            "Mean pooling + context length": "collision removed",
            "Sum pooling": "collision removed",
        },
        value="Mean pooling (paper)",
        label="Architecture",
    )
    architecture
    return (architecture,)


@app.cell
def _(architecture, mo):
    mo.callout(
        f"Selected control: **{architecture.value}**.",
        kind="danger" if architecture.value == "collision remains" else "success",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Why the other claims survive

    **Claim 1.** Expanding squared loss leaves a cross-term whose conditional
    expectation is zero.

    **Claim 3.** The stated conditional MGF yields the displayed concentration
    constant; posterior odds, total variance, and Bayes-risk ≤ minimax complete
    the proof.

    **Claim 4.** A direct coupling bounds the source-target expectation change by
    the exact prompt Wasserstein distance. Posterior variance is model-independent
    within the target domain, but need not equal its source value.

    **Claim 5.** `Q=K=0` makes every score zero, so softmax assigns exact weight
    `1/k` and the attention output is the mean of values.

    ## Reproduce

    The formal cumulative command is:

    ```bash
    uv run --locked python repro/src/verify.py
    ```

    See the [illustrated report](https://github.com/MachineLearning-Nerd/icml26-repro-BUFSSOuphA-in-context-learning-is-provably-bayesian-inference-a-generalization-theory-f/blob/main/reports/reproduction/report.md)
    and [candidate logbook](https://huggingface.co/spaces/DineshAI/BUFSSOuphA).
    """)
    return


if __name__ == "__main__":
    app.run()
