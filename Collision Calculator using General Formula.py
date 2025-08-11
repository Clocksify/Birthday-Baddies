from fractions import Fraction
from math import comb, factorial

#use Fraction for exact arithmetic

def perm(a: int, k: int) -> int:
    """P(a,k) = a!/(a-k)!  (0 if k>a or k<0)."""
    if k < 0 or k > a:
        return 0
    prod = 1
    for i in range(k):
        prod *= (a - i)
    return prod

def single_term(N: int, q: int, K: int, c: int | Fraction, m: int) -> Fraction:
    #sums up the terms in the sigma notation for a given m
    #will repeat this later as m increases until m = q
    c = Fraction(c, 1)
    p = Fraction(1, c*K + (N - K))
    cp = c * p

    return (Fraction(comb(q, m), 1) *
            Fraction(perm(K, m), 1) *
            Fraction(perm(N - K, q - m), 1) *
            (cp ** m) *
            (p ** (q - m)))

def sum_modified(N: int, q: int, K: int, c: int | Fraction):
    c = Fraction(c, 1)
    p = Fraction(1, c*K + (N - K))  

    total = Fraction(0, 1)
    for m in range(q + 1):
        if m > K or (q - m) > (N - K):
            continue
        total += single_term(N, q, K, c, m)
    #total is sum of terms for q number of balls thrown

    S = Fraction(1, 1) - total
    return S, float(S)

# Alternative form using q! * C(K,m) * C(N-K, q-m) instead
def sum_modified_alt(N: int, q: int, K: int, c: int | Fraction):
    c = Fraction(c, 1)
    p = Fraction(1, c*K + (N - K))
    cp = c * p

    q_fact = Fraction(factorial(q), 1)
    total = Fraction(0, 1)
    for m in range(q + 1):
        if m > K or (q - m) > (N - K):
            continue
        coeff = q_fact * Fraction(comb(K, m), 1) * Fraction(comb(N - K, q - m), 1)
        total += coeff * (cp ** m) * (p ** (q - m))

    S = Fraction(1, 1) - total
    return S, float(S)

N, q, K, c = 8, 3, 4, 4
frac_val, dec_val = sum_modified(N, q, K, c)
print("Exact:", frac_val) 
print("Decimal:", dec_val)
