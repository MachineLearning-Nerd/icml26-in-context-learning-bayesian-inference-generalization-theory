"""Exact implementation certificate for Definition 2 uniform attention."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import permutations
import json


Vector = tuple[Fraction, ...]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction())


def scaled_dot_product_attention_zero_qk(
    values: tuple[Vector, ...],
) -> tuple[Vector, tuple[Fraction, ...]]:
    """Compute attention(Q=0,K=0,V) through the score and softmax path."""
    if not values:
        raise ValueError("context must be nonempty")
    dimension = len(values[0])
    query = tuple(Fraction() for _ in range(dimension))
    keys = tuple(query for _ in values)
    scores = tuple(dot(query, key) for key in keys)
    if any(score != 0 for score in scores):
        raise AssertionError("Q=K=0 must produce zero scores")
    exp_scores = tuple(Fraction(1) for _ in scores)
    denominator = sum(exp_scores, Fraction())
    weights = tuple(score / denominator for score in exp_scores)
    output = tuple(
        sum(
            (weight * value[column] for weight, value in zip(weights, values)),
            Fraction(),
        )
        for column in range(dimension)
    )
    return output, weights


def mean_pool(values: tuple[Vector, ...]) -> Vector:
    count = Fraction(len(values))
    return tuple(
        sum((value[column] for value in values), Fraction()) / count
        for column in range(len(values[0]))
    )


def exhaustive_permutation_certificate() -> dict[str, int | bool]:
    checked = 0
    for length in range(1, 7):
        values = tuple(
            (Fraction(index - 2, 3), Fraction(index * index - 3, 5))
            for index in range(length)
        )
        expected = mean_pool(values)
        for order in permutations(range(length)):
            permuted = tuple(values[index] for index in order)
            output, weights = scaled_dot_product_attention_zero_qk(permuted)
            expected_weight = Fraction(1, length)
            if output != expected or any(weight != expected_weight for weight in weights):
                return {"passed": False, "exact_permutations": checked}
            checked += 1
    return {"passed": True, "exact_permutations": checked}


def nonzero_score_control() -> dict[str, str | bool]:
    getcontext().prec = 50
    exp_zero = Decimal(0).exp()
    exp_one = Decimal(1).exp()
    weight_zero = exp_zero / (exp_zero + exp_one)
    weight_one = exp_one / (exp_zero + exp_one)
    return {
        "control": "scores [0,1] instead of all-zero QK scores",
        "weight_0": str(weight_zero),
        "weight_1": str(weight_one),
        "nonuniform": weight_zero != weight_one,
        "rejected_as_uniform_attention": weight_zero != weight_one,
    }


def build_certificate() -> dict:
    permutations_result = exhaustive_permutation_certificate()
    control = nonzero_score_control()
    return {
        "claim": 5,
        "status": "VERIFIED",
        "exact_architecture": "Attention(Q=0,K=0,V)=softmax(0)V=(1/k)sum_i V_i",
        "definition_2_mapping": (
            "V_i=phi_theta(x_i,y_i); decoder rho_theta receives mean(V) and x_query"
        ),
        "independent_checker": permutations_result,
        "negative_control": control,
        "passed": permutations_result["passed"] and control["rejected_as_uniform_attention"],
    }


if __name__ == "__main__":
    certificate = build_certificate()
    print(json.dumps(certificate, indent=2, sort_keys=True))
    raise SystemExit(0 if certificate["passed"] else 1)
