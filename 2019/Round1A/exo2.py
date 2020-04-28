
def bezout(a, b):
    """returns u, v such as au+bv = pgcd(a,b)"""
    if b == 0:
        return (1, 0)
    else:
        (u, v) = bezout(b, a % b)
        return (v, u - (a // b) * v)


def chinese_theorem_inv(modulo_list):
    """
    Returns (x, n1*...*nk) such as
    x mod mk = ak for all k, with
    modulo_list = [(a1, n1), ..., (ak, nk)]
    n1, ..., nk most be coprime 2 by 2.
    """
    a, n = modulo_list[0]
    for a2, n2 in modulo_list[1:]:
        u, v = bezout(n, n2)
        a, n = a*v*n2+a2*u*n, n*n2

    for (a1, n1) in modulo_list:
        assert a % n1 == a1

    return ((n+a % n) % n, n)


T, N, M = [int(x) for x in input().split()]

for t in range(1, T+1):

    eq = []
    for n in [5, 7, 11, 13, 17, 18]:
        print(*[n]*18, flush=True)
        a = sum(int(x) for x in input().split()) % n
        eq.append((a, n))

    res, _ = chinese_theorem_inv(eq)
    print(res % M, flush=True)

    if int(input()) == -1:
        exit()
