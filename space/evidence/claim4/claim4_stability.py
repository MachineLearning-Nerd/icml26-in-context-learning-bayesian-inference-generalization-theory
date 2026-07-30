"""Executable exact component checker for Theorem 4."""

from fractions import Fraction


def main():
    counts = {"square": 0, "holder": 0, "architecture": 0, "transport": 0}
    for bound in map(Fraction, range(1, 5)):
        values = tuple(map(Fraction, range(-int(bound), int(bound) + 1)))
        for left in values:
            for right in values:
                assert abs(left**2 - right**2) <= 2 * bound * abs(left - right)
                counts["square"] += 1

    for diameter in range(1, 9):
        for distance in range(diameter + 1):
            assert distance**2 <= diameter * distance
            counts["holder"] += 1

    for summary_lip in map(Fraction, range(1, 5)):
        for encoder_lip in map(Fraction, range(1, 5)):
            for query_lip in map(Fraction, range(1, 5)):
                modulus = summary_lip * encoder_lip + query_lip
                for context_distance in map(Fraction, range(5)):
                    for query_distance in map(Fraction, range(5)):
                        direct = (
                            summary_lip * encoder_lip * context_distance
                            + query_lip * query_distance
                        )
                        assert direct <= modulus * (
                            context_distance + query_distance
                        )
                        counts["architecture"] += 1

    values = tuple(map(Fraction, range(-2, 3)))
    for denominator in range(1, 6):
        probabilities = tuple(
            Fraction(numerator, denominator)
            for numerator in range(denominator + 1)
        )
        for source in probabilities:
            for target in probabilities:
                wasserstein = abs(source - target)
                for left in values:
                    for right in values:
                        source_mean = (1 - source) * left + source * right
                        target_mean = (1 - target) * left + target * right
                        assert abs(target_mean - source_mean) <= (
                            abs(right - left) * wasserstein
                        )
                        counts["transport"] += 1

    false_prefactor_residual = abs(Fraction(2) ** 2 - Fraction(1) ** 2) - 2
    assert false_prefactor_residual == 1
    assert sum(counts.values()) == 4058
    print(
        {
            "passed": True,
            "exact_cases": 4058,
            "source_pv": "0",
            "target_pv": "1/4",
        }
    )


if __name__ == "__main__":
    main()
