"""Executable exact counterexample checker for Theorem 2."""

from fractions import Fraction
from itertools import product


PRIOR = {Fraction(-1): Fraction(1, 2), Fraction(1): Fraction(1, 2)}
NOISE = {
    Fraction(-2): Fraction(1, 4),
    Fraction(0): Fraction(1, 2),
    Fraction(2): Fraction(1, 4),
}
YS = tuple(map(Fraction, (-3, -1, 1, 3)))


def likelihood(observations, task):
    result = Fraction(1)
    for observation in observations:
        result *= NOISE.get(observation - task, Fraction())
    return result


def probability(observations):
    return sum(
        (prior * likelihood(observations, task) for task, prior in PRIOR.items()),
        Fraction(),
    )


def posterior_mean(observations):
    denominator = probability(observations)
    numerator = sum(
        (
            prior * likelihood(observations, task) * task
            for task, prior in PRIOR.items()
        ),
        Fraction(),
    )
    return numerator / denominator


def main():
    assert sum(NOISE.values(), Fraction()) == 1
    assert sum(
        (value * mass for value, mass in NOISE.items()), Fraction()
    ) == 0
    assert sum(
        (value**2 * mass for value, mass in NOISE.items()), Fraction()
    ) == 2

    holder_cases = 0
    max_ratio = Fraction()
    for length in (1, 2):
        prompts = tuple(
            values
            for values in product(YS, repeat=length)
            if probability(values) > 0
        )
        for left in prompts:
            for right in prompts:
                distance = sum(
                    (abs(a - b) for a, b in zip(left, right)), Fraction()
                ) / length
                difference = abs(posterior_mean(left) - posterior_mean(right))
                if distance:
                    max_ratio = max(max_ratio, difference / distance)
                else:
                    assert difference == 0
                holder_cases += 1
    assert holder_cases == 212
    assert max_ratio <= 1

    one = (Fraction(1),)
    two = (Fraction(1), Fraction(1))
    q1, q2 = probability(one), probability(two)
    mu1, mu2 = posterior_mean(one), posterior_mean(two)
    shared = (q1 * mu1 + q2 * mu2) / (q1 + q2)
    lower_bound = Fraction(1, 2) * (
        q1 * (shared - mu1) ** 2 + q2 * (shared - mu2) ** 2
    )
    assert (q1, q2, mu1, mu2, shared, lower_bound) == (
        Fraction(3, 8),
        Fraction(5, 32),
        Fraction(1, 3),
        Fraction(3, 5),
        Fraction(7, 17),
        Fraction(1, 255),
    )
    print(
        {
            "status": "FALSIFIED",
            "holder_cases": holder_cases,
            "bayes_means": ["1/3", "3/5"],
            "uniform_lower_bound": "1/255",
        }
    )


if __name__ == "__main__":
    main()
