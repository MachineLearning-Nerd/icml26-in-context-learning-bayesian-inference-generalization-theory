"""Independent closed-form checker; imports no campaign code."""

from fractions import Fraction


a, b = Fraction(1, 2), Fraction(1, 4)
q1, q2 = (a + b) / 2, (a**2 + b**2) / 2
mu1, mu2 = (a - b) / (a + b), (a**2 - b**2) / (a**2 + b**2)
v = (q1 * mu1 + q2 * mu2) / (q1 + q2)
lower = Fraction(1, 2) * (q1 * (v - mu1) ** 2 + q2 * (v - mu2) ** 2)
observed = (q1, q2, mu1, mu2, v, lower)
expected = (
    Fraction(3, 8),
    Fraction(5, 32),
    Fraction(1, 3),
    Fraction(3, 5),
    Fraction(7, 17),
    Fraction(1, 255),
)
assert observed == expected
print({"passed": True, "observed": [str(value) for value in observed]})
