"""Independent closed-form checker for the Claim 2 counterexample."""

from __future__ import annotations

from fractions import Fraction


def independent_certificate() -> dict:
    likelihood_plus = Fraction(1, 2)
    likelihood_minus = Fraction(1, 4)
    probability_one = (likelihood_plus + likelihood_minus) / 2
    probability_two = (likelihood_plus**2 + likelihood_minus**2) / 2
    mean_one = (likelihood_plus - likelihood_minus) / (
        likelihood_plus + likelihood_minus
    )
    mean_two = (likelihood_plus**2 - likelihood_minus**2) / (
        likelihood_plus**2 + likelihood_minus**2
    )
    prediction = (
        probability_one * mean_one + probability_two * mean_two
    ) / (probability_one + probability_two)
    lower_bound = Fraction(1, 2) * (
        probability_one * (prediction - mean_one) ** 2
        + probability_two * (prediction - mean_two) ** 2
    )
    expected = (
        Fraction(3, 8),
        Fraction(5, 32),
        Fraction(1, 3),
        Fraction(3, 5),
        Fraction(7, 17),
        Fraction(1, 255),
    )
    observed = (
        probability_one,
        probability_two,
        mean_one,
        mean_two,
        prediction,
        lower_bound,
    )
    return {
        "implementation": "closed form; does not import claim2_counterexample",
        "observed": [str(value) for value in observed],
        "expected": [str(value) for value in expected],
        "passed": observed == expected,
    }
