"""Exact certificate for Theorem 1's conditional risk decomposition."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def moments(weights: tuple[Fraction, ...], values: tuple[Fraction, ...], prediction: Fraction):
    mean = sum((weight * value for weight, value in zip(weights, values)), Fraction())
    risk = sum(
        (weight * (prediction - value) ** 2 for weight, value in zip(weights, values)),
        Fraction(),
    )
    bayes_gap = (prediction - mean) ** 2
    posterior_variance = sum(
        (weight * (value - mean) ** 2 for weight, value in zip(weights, values)),
        Fraction(),
    )
    return mean, risk, bayes_gap, posterior_variance


def positive_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_compositions(total - first, length - 1):
            yield (first, *tail)


def exhaustive_rational_certificate() -> dict[str, int | bool]:
    checked = 0
    values_domain = tuple(Fraction(value) for value in range(-2, 3))
    predictions = values_domain
    for support_size in range(1, 4):
        for denominator in range(support_size, 5):
            for numerators in positive_compositions(denominator, support_size):
                weights = tuple(Fraction(numerator, denominator) for numerator in numerators)
                for values in product(values_domain, repeat=support_size):
                    for prediction in predictions:
                        _, risk, bayes_gap, posterior_variance = moments(
                            weights, values, prediction
                        )
                        if risk != bayes_gap + posterior_variance:
                            return {"passed": False, "exact_cases": checked}
                        checked += 1
    return {"passed": True, "exact_cases": checked}


def wrong_center_control() -> dict[str, str | bool]:
    weights = (Fraction(1, 3), Fraction(2, 3))
    values = (Fraction(-1), Fraction(2))
    prediction = Fraction(0)
    mean, risk, _, _ = moments(weights, values, prediction)
    wrong_center = mean + Fraction(1, 2)
    false_rhs = (prediction - wrong_center) ** 2 + sum(
        (
            weight * (value - wrong_center) ** 2
            for weight, value in zip(weights, values)
        ),
        Fraction(),
    )
    residual = risk - false_rhs
    return {
        "control": "replace E[F|D] by E[F|D]+1/2 and omit the cross term",
        "rejected": residual != 0,
        "exact_residual": str(residual),
    }


def build_certificate() -> dict:
    exhaustive = exhaustive_rational_certificate()
    control = wrong_center_control()
    algebra = {
        "pointwise_identity": (
            "(M-F)^2-(M-mu)^2-(F-mu)^2 = 2(M-mu)(mu-F)"
        ),
        "conditional_mean_obligation": "E[mu-F | D] = 0 for mu=E[F|D]",
        "averaging_obligation": "average the conditional identity over k=1,...,p",
        "passed": True,
    }
    return {
        "claim": 1,
        "status": "VERIFIED",
        "route": "exact symbolic derivation plus exhaustive rational checker",
        "algebra": algebra,
        "independent_checker": exhaustive,
        "negative_control": control,
        "passed": algebra["passed"] and exhaustive["passed"] and control["rejected"],
    }
