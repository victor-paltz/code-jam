
import sys
from math import pi
# from functools import lru_cache


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


def solve2(k, tab):
    n = len(tab)
    f = [-float("inf")]*(k+1)
    f[0] = 0
    for i in range(n):
        r, h = tab[i]
        for k1 in reversed(range(1, k+1)):
            f[k1] = max(f[k1-1]+2*r*h + (r*r if k1 == k else 0), f[k1])
    return f[k]

# That version doesn't pass test 2 (Runtime Error) on
# the google code jam website.
# Yet, it's exactly the same as solve2 function...
# I have no clue about that one...

# @lru_cache(None)
# def solve(i, k, n):
#     if i >= n:
#         if k == 0:
#             return 0
#         return -float("inf")
#     if k > 0:
#         r, h = pancakes[i]
#         return max(solve(i+1, k-1, n)+2*r*h + (r*r if k == 1 else 0), solve(i+1, k, n))
#     return solve(i+1, k, n)


T = readint()

for test in range(1, T+1):

    N, K = readints()

    pancakes = readinttab(N)
    pancakes.sort()

    # solve.cache_clear()
    # sol = solve(0, K, N)*pi

    sol = solve2(K, pancakes)*pi

    print("Case #{}: {:.7f}".format(test, sol))
