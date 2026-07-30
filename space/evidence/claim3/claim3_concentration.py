"""Executable exact checker for Theorem 3."""

from fractions import Fraction
from itertools import product


def positive_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_compositions(total - first, length - 1):
            yield (first, *tail)


def check_bernstein_rate():
    checked = 0
    for divergence in map(Fraction, range(1, 7)):
        for variance_scale in map(Fraction, range(1, 7)):
            for tail_scale in map(Fraction, range(1, 7)):
                denominator = variance_scale + tail_scale * divergence / 2
                chernoff_lambda = divergence / (2 * denominator)
                achieved = (
                    chernoff_lambda * divergence / 2
                    - chernoff_lambda**2 * variance_scale / 2
                )
                stated = divergence**2 / (8 * denominator)
                assert tail_scale * chernoff_lambda <= 1
                assert achieved >= stated
                checked += 1
    return checked


def mixture_variance(weights, means, variances):
    mean = sum((w * value for w, value in zip(weights, means)), Fraction())
    return sum(
        (
            w * (variance + (value - mean) ** 2)
            for w, value, variance in zip(weights, means, variances)
        ),
        Fraction(),
    )


def check_mixture_variance():
    checked = 0
    values = tuple(map(Fraction, (-1, 0, 1)))
    variance_values = (Fraction(), Fraction(1, 2), Fraction(1))
    for task_count in (2, 3):
        for denominator in range(task_count, 5):
            for nums in positive_compositions(denominator, task_count):
                weights = tuple(Fraction(value, denominator) for value in nums)
                for means in product(values, repeat=task_count):
                    for variances in product(variance_values, repeat=task_count):
                        assert mixture_variance(weights, means, variances) <= (
                            variances[0] + 5 * (1 - weights[0])
                        )
                        checked += 1
    return checked


def check_posterior_odds():
    checked = 0
    likelihood_ratios = tuple(Fraction(value, 4) for value in range(5))
    for task_count in (2, 3):
        for denominator in range(task_count, 7):
            for nums in positive_compositions(denominator, task_count):
                priors = tuple(Fraction(value, denominator) for value in nums)
                for ratios in product(likelihood_ratios, repeat=task_count - 1):
                    odds = sum(
                        (
                            priors[index] / priors[0] * ratios[index - 1]
                            for index in range(1, task_count)
                        ),
                        Fraction(),
                    )
                    assert odds / (1 + odds) <= odds
                    checked += 1
    return checked


def check_bayes_minimax():
    checked = 0
    values = tuple(map(Fraction, (-1, 0, 1)))
    predictions = tuple(Fraction(value, 4) for value in range(-4, 5))
    for support_size in (1, 2, 3):
        for functions in product(values, repeat=support_size):
            for denominator in range(support_size, 6):
                for nums in positive_compositions(denominator, support_size):
                    prior = tuple(Fraction(value, denominator) for value in nums)
                    mean = sum(
                        (weight * value for weight, value in zip(prior, functions)),
                        Fraction(),
                    )
                    bayes = sum(
                        (
                            weight * (value - mean) ** 2
                            for weight, value in zip(prior, functions)
                        ),
                        Fraction(),
                    )
                    minimax = min(
                        max((value - prediction) ** 2 for value in functions)
                        for prediction in predictions
                    )
                    assert bayes <= minimax
                    checked += 1
    return checked


def main():
    counts = {
        "bernstein_rate": check_bernstein_rate(),
        "mixture_variance": check_mixture_variance(),
        "posterior_odds": check_posterior_odds(),
        "bayes_minimax": check_bayes_minimax(),
    }
    weights = (Fraction(7, 8), Fraction(1, 8))
    residual = mixture_variance(
        weights, (Fraction(-1), Fraction(1)), (Fraction(), Fraction())
    ) - 3 * (1 - weights[0])
    assert residual == Fraction(1, 16)
    assert sum(counts.values()) == 4568
    print({"passed": True, "exact_cases": 4568, "control_residual": str(residual)})


if __name__ == "__main__":
    main()
