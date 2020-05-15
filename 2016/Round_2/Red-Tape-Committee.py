
import sys
from functools import lru_cache


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


def get_proba(Pi, e):
    """"
    O(k^2)
    """
    @lru_cache(None)
    def p_e_true(n, e):
        if n < 0:
            return 1 if e == 0 else 0
        if abs(e) > n+1:
            return 0
        return Pi[n]*p_e_true(n-1, e-1) + (100-Pi[n])*p_e_true(n-1, e+1)

    return p_e_true(len(Pi)-1, e)


T = readint()

for t in range(1, T+1):

    N, K = readints()

    Pi = [round(float(x)*100) for x in readstr().split()]

    # O(N*Log(N))
    Pi.sort()

    # O(Kˆ3)
    best = 0
    for k in range(K+1):
        best = max(best, get_proba(Pi[:k]+Pi[N-(K-k):], 0))

    print("Case #{}: {:.7f}".format(t, best/100**K))
