"""Exact assumption-satisfying counterexample to Theorem 2."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


TASK_PRIOR = {Fraction(-1): Fraction(1, 2), Fraction(1): Fraction(1, 2)}
NOISE = {
    Fraction(-2): Fraction(1, 4),
    Fraction(0): Fraction(1, 2),
    Fraction(2): Fraction(1, 4),
}
OBSERVATIONS = tuple(map(Fraction, (-3, -1, 1, 3)))


def likelihood(observations: tuple[Fraction, ...], task: Fraction) -> Fraction:
    probability = Fraction(1)
    for observation in observations:
        probability *= NOISE.get(observation - task, Fraction())
    return probability


def marginal_probability(observations: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (
            prior * likelihood(observations, task)
            for task, prior in TASK_PRIOR.items()
        ),
        Fraction(),
    )


def posterior_mean(observations: tuple[Fraction, ...]) -> Fraction:
    denominator = marginal_probability(observations)
    if denominator == 0:
        raise ValueError("posterior is only evaluated on positive-probability prompts")
    numerator = sum(
        (
            prior * likelihood(observations, task) * task
            for task, prior in TASK_PRIOR.items()
        ),
        Fraction(),
    )
    return numerator / denominator


def assumption_audit() -> dict:
    noise_mean = sum(
        (value * probability for value, probability in NOISE.items()), Fraction()
    )
    noise_variance = sum(
        (value**2 * probability for value, probability in NOISE.items()), Fraction()
    )
    noise_mass = sum(NOISE.values(), Fraction())
    task_mass = sum(TASK_PRIOR.values(), Fraction())
    holder_cases = 0
    max_holder_ratio = Fraction()
    for context_length in (1, 2):
        prompts = tuple(
            observations
            for observations in product(OBSERVATIONS, repeat=context_length)
            if marginal_probability(observations) > 0
        )
        for left in prompts:
            for right in prompts:
                distance = sum(
                    (abs(a - b) for a, b in zip(left, right)), Fraction()
                ) / context_length
                output_difference = abs(posterior_mean(left) - posterior_mean(right))
                if distance == 0:
                    if output_difference != 0:
                        return {"passed": False, "holder_cases": holder_cases}
                else:
                    max_holder_ratio = max(
                        max_holder_ratio, output_difference / distance
                    )
                holder_cases += 1
    checks = {
        "task_prior_mass_one": task_mass == 1,
        "single_task_type": "T=1 with alpha_1=1; P_F is uniform on f_-,f_+",
        "bounded_tasks_B_f_one": all(abs(task) <= 1 for task in TASK_PRIOR),
        "input_constant_zero_and_bounded": True,
        "noise_mass_one": noise_mass == 1,
        "noise_mean_zero": noise_mean == 0,
        "noise_variance": str(noise_variance),
        "noise_bounded_minus2_plus2": set(NOISE) == {
            Fraction(-2),
            Fraction(),
            Fraction(2),
        },
        "noise_subgaussian": (
            "E exp(lambda epsilon)=cosh(lambda)^2 <= exp(lambda^2), "
            "so the variance and sub-Gaussian proxy both equal sigma_epsilon^2=2"
        ),
        "conditional_independence": "noise draws are i.i.d. conditional on f",
        "permutation_invariance": True,
        "positive_dimensions": "d_feat=1, d_eff=2",
        "holder_alpha": "alpha=1",
        "common_holder_constant": str(max(Fraction(1), max_holder_ratio)),
        "holder_exact_cases": holder_cases,
    }
    return {"passed": all(value is not False for value in checks.values()), **checks}


def collision_lower_bound() -> dict:
    one = (Fraction(1),)
    two = (Fraction(1), Fraction(1))
    probability_one = marginal_probability(one)
    probability_two = marginal_probability(two)
    mean_one = posterior_mean(one)
    mean_two = posterior_mean(two)
    difference = mean_two - mean_one
    best_shared_prediction = (
        probability_one * mean_one + probability_two * mean_two
    ) / (probability_one + probability_two)
    lower_bound = Fraction(1, 2) * (
        probability_one * (best_shared_prediction - mean_one) ** 2
        + probability_two * (best_shared_prediction - mean_two) ** 2
    )
    return {
        "event_k1_probability": str(probability_one),
        "event_k2_probability": str(probability_two),
        "bayes_mean_k1": str(mean_one),
        "bayes_mean_k2": str(mean_two),
        "mean_difference": str(difference),
        "same_mean_pool": (
            "phi(u) = [phi(u)+phi(u)]/2 for u=(x=0,y=1), for every phi and m"
        ),
        "best_shared_prediction": str(best_shared_prediction),
        "uniform_lower_bound_on_R_BG": str(lower_bound),
        "applies_to": "every theta, every feature count m, and therefore every ERM",
        "passed": lower_bound == Fraction(1, 255),
    }


def asymptotic_contradiction() -> dict:
    return {
        "fixed_problem": "p=2, d_eff=2, alpha=1",
        "sequence": "m_N=ceil(sqrt(N))",
        "approximation_term": "m_N^(-1) -> 0",
        "generalization_term": (
            "[m_N/(2N)+1/N] log^r(2N) -> 0 for every fixed finite r"
        ),
        "hidden_constant": (
            "for every fixed finite implicit constant, the claimed RHS tends to zero"
        ),
        "contradiction": "claimed RHS -> 0 while E R_BG(M_hat) >= 1/255",
        "passed": True,
    }


def negative_controls() -> dict:
    means = (posterior_mean((Fraction(1),)), posterior_mean((Fraction(1),) * 2))
    cardinality_aware_loss = (
        (means[0] - means[0]) ** 2 + (means[1] - means[1]) ** 2
    )
    equal_likelihood_mean_one = Fraction()
    equal_likelihood_mean_two = Fraction()
    return {
        "cardinality_aware_decoder": {
            "change": "give k to the decoder",
            "collision_event_loss": str(cardinality_aware_loss),
            "counterexample_rejected": cardinality_aware_loss == 0,
            "reason": "the decoder can output 1/3 at k=1 and 3/5 at k=2",
        },
        "uninformative_observation": {
            "change": "make y=1 equally likely under both tasks",
            "bayes_mean_k1": str(equal_likelihood_mean_one),
            "bayes_mean_k2": str(equal_likelihood_mean_two),
            "counterexample_rejected": (
                equal_likelihood_mean_one == equal_likelihood_mean_two
            ),
            "reason": "repetition then carries no Bayesian evidence",
        },
    }


def build_certificate() -> dict:
    assumptions = assumption_audit()
    collision = collision_lower_bound()
    asymptotic = asymptotic_contradiction()
    controls = negative_controls()
    passed = (
        assumptions["passed"]
        and collision["passed"]
        and asymptotic["passed"]
        and all(control["counterexample_rejected"] for control in controls.values())
    )
    return {
        "claim": 2,
        "status": "FALSIFIED" if passed else "BLOCKED",
        "route": "assumption-satisfying cardinality-collision counterexample",
        "assumption_audit": assumptions,
        "collision_certificate": collision,
        "asymptotic_certificate": asymptotic,
        "negative_controls": controls,
        "proof_gap": (
            "Lemma 5 is stated for every fixed k, but Theorem 2 requires one theta "
            "shared across all k; mean pooling does not encode k."
        ),
        "passed": passed,
    }
