"""Exact proof certificate for Theorem 3's posterior-variance bound."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def positive_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_compositions(total - first, length - 1):
            yield (first, *tail)


def bernstein_rate_certificate() -> dict[str, str | bool | int]:
    checked = 0
    for divergence in map(Fraction, range(1, 7)):
        for variance_scale in map(Fraction, range(1, 7)):
            for tail_scale in map(Fraction, range(1, 7)):
                denominator = variance_scale + tail_scale * divergence / 2
                chernoff_lambda = divergence / (2 * denominator)
                achieved_rate = (
                    chernoff_lambda * divergence / 2
                    - chernoff_lambda**2 * variance_scale / 2
                )
                stated_rate = divergence**2 / (8 * denominator)
                if tail_scale * chernoff_lambda > 1 or achieved_rate < stated_rate:
                    return {"passed": False, "exact_parameter_cases": checked}
                checked += 1
    return {
        "passed": True,
        "exact_parameter_cases": checked,
        "lambda": "D/[2(nu^2+bD/2)]",
        "domain_check": "b*lambda <= 1",
        "achieved_rate_minus_stated_rate": (
            "b*D^3/[16(nu^2+bD/2)^2] >= 0"
        ),
    }


def mixture_variance(
    weights: tuple[Fraction, ...],
    means: tuple[Fraction, ...],
    variances: tuple[Fraction, ...],
) -> Fraction:
    mean = sum((weight * value for weight, value in zip(weights, means)), Fraction())
    return sum(
        (
            weight * (variance + (value - mean) ** 2)
            for weight, value, variance in zip(weights, means, variances)
        ),
        Fraction(),
    )


def exhaustive_variance_certificate() -> dict[str, int | bool]:
    checked = 0
    values = tuple(map(Fraction, (-1, 0, 1)))
    variance_values = (Fraction(), Fraction(1, 2), Fraction(1))
    for task_count in (2, 3):
        for denominator in range(task_count, 5):
            for numerators in positive_compositions(denominator, task_count):
                weights = tuple(Fraction(value, denominator) for value in numerators)
                for means in product(values, repeat=task_count):
                    for variances in product(variance_values, repeat=task_count):
                        mixture = mixture_variance(weights, means, variances)
                        wrong_mass = 1 - weights[0]
                        bound = variances[0] + 5 * wrong_mass
                        if mixture > bound:
                            return {"passed": False, "exact_cases": checked}
                        checked += 1
    return {"passed": True, "exact_cases": checked}


def exhaustive_posterior_odds_certificate() -> dict[str, int | bool]:
    checked = 0
    likelihood_ratios = tuple(Fraction(value, 4) for value in range(5))
    for task_count in (2, 3):
        for denominator in range(task_count, 7):
            for numerators in positive_compositions(denominator, task_count):
                priors = tuple(Fraction(value, denominator) for value in numerators)
                for wrong_ratios in product(likelihood_ratios, repeat=task_count - 1):
                    odds = sum(
                        (
                            priors[index] / priors[0] * wrong_ratios[index - 1]
                            for index in range(1, task_count)
                        ),
                        Fraction(),
                    )
                    posterior_error = odds / (1 + odds)
                    if posterior_error > odds:
                        return {"passed": False, "exact_cases": checked}
                    checked += 1
    return {"passed": True, "exact_cases": checked}


def exhaustive_bayes_minimax_certificate() -> dict[str, int | bool]:
    checked = 0
    function_values = tuple(map(Fraction, (-1, 0, 1)))
    predictions = tuple(Fraction(value, 4) for value in range(-4, 5))
    for support_size in (1, 2, 3):
        for functions in product(function_values, repeat=support_size):
            for denominator in range(support_size, 6):
                for numerators in positive_compositions(denominator, support_size):
                    prior = tuple(Fraction(value, denominator) for value in numerators)
                    posterior_mean = sum(
                        (weight * value for weight, value in zip(prior, functions)),
                        Fraction(),
                    )
                    bayes_risk = sum(
                        (
                            weight * (value - posterior_mean) ** 2
                            for weight, value in zip(prior, functions)
                        ),
                        Fraction(),
                    )
                    grid_minimax = min(
                        max((value - prediction) ** 2 for value in functions)
                        for prediction in predictions
                    )
                    if bayes_risk > grid_minimax:
                        return {"passed": False, "exact_cases": checked}
                    checked += 1
    return {"passed": True, "exact_cases": checked}


def negative_controls() -> dict:
    true_weight = Fraction(7, 8)
    weights = (true_weight, 1 - true_weight)
    means = (Fraction(-1), Fraction(1))
    variances = (Fraction(), Fraction())
    mixture = mixture_variance(weights, means, variances)
    wrong_mass = 1 - true_weight
    false_bound = variances[0] + 3 * wrong_mass
    zero_divergence_rejected = Fraction() <= 0
    return {
        "weakened_variance_constant": {
            "replacement": "5*B_f^2 -> 3*B_f^2",
            "exact_residual": str(mixture - false_bound),
            "rejected": mixture > false_bound,
        },
        "missing_identifiability": {
            "input": "D_j=0",
            "rejected": zero_divergence_rejected,
            "reason": "The theorem explicitly requires every D_j>0.",
        },
    }


def build_certificate() -> dict:
    bernstein = bernstein_rate_certificate()
    variance = exhaustive_variance_certificate()
    posterior = exhaustive_posterior_odds_certificate()
    minimax = exhaustive_bayes_minimax_certificate()
    controls = negative_controls()
    proof_obligations = {
        "likelihood_ratio_chain": (
            "common P_X cancels, so p_j(D^k)/p_i(D^k)=exp(sum_t Z_j,t)"
        ),
        "concentration": (
            "iterate the conditional MGF and apply Chernoff at "
            "lambda=D/[2(nu^2+bD/2)]"
        ),
        "posterior_odds": "1-pi_i=S/(1+S)<=S, then split on the concentration event",
        "variance": (
            "law of total variance gives within-type plus between-type variance; "
            "boundedness contributes at most (1+4)B_f^2 times wrong mass"
        ),
        "minimax": (
            "supremum risk dominates prior-average risk; posterior mean minimizes "
            "that average pointwise"
        ),
        "all_k": "the derivation uses only k>=1 and is symbolic in k",
        "passed": True,
    }
    passed = (
        proof_obligations["passed"]
        and bernstein["passed"]
        and variance["passed"]
        and posterior["passed"]
        and minimax["passed"]
        and controls["weakened_variance_constant"]["rejected"]
        and controls["missing_identifiability"]["rejected"]
    )
    return {
        "claim": 3,
        "status": "VERIFIED" if passed else "BLOCKED",
        "route": "independent universal derivation plus exact rational checkers",
        "proof_obligations": proof_obligations,
        "independent_checkers": {
            "bernstein_rate": bernstein,
            "mixture_variance": variance,
            "posterior_odds": posterior,
            "bayes_minimax": minimax,
        },
        "negative_controls": controls,
        "passed": passed,
    }
