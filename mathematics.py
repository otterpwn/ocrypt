from typing import List
import numpy as np


def quadResidues(p: int, ints: List[int]) -> List[int]:
    return [x for x in range(p) if pow(x, 2, p) in ints]


def legendreSymbol(a: int, p: int) -> int:
    assert p % 2 != 0
    return pow(a, (p - 1) >> 1, p)


def tonelliShanks(n: int, p: int) -> int:
    assert legendreSymbol(n, p) == 1, "[!] n is not a square (mod p)"
    q = p - 1
    s = 0

    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendreSymbol(z, p):
            break

    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0

    while (t - 1) % p != 0:
        t2 = (t * t) % p

        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p

        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def chineseReminder(a: List[int], m: List[int]) -> int:
    from Crypto.Util.number import inverse
    mul = 1
    for i in m:
        mul *= i

    M = [mul // x for x in m]
    y = [inverse(M[i], m[i]) for i in range(len(m))]

    ans = 0

    for i in range(len(m)):
        ans += a[i] * M[i] * y[i]

    return ans % mul


def gramSchmidt(u: np.ndarray, vectors: List[np.ndarray]) -> List[np.ndarray]:
    for i in range(1, len(vectors)):
        mi = [np.dot(vectors[i], u[j]) / np.dot(u[j], u[j])
              for j in range(len(u))]
        u += [vectors[i] - sum([mij * uj for (mij, uj) in zip(mi, u)])]

    return u


def gaussianReduction(v1: np.ndarray, v2: np.ndarray) -> int:
    while True:
        if (np.dot(v2, v2) < np.dot(v1, v1)):
            v1, v2 = v2, v1
        m = int((v1.dot(v2)) / (v1.dot(v1)))

        if m == 0:
            return (v1.dot(v2))

        v2 = v2 - m * v1
