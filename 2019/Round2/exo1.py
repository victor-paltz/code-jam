
from fractions import Fraction as frac
from itertools import combinations
import sys


def readint():
    return int(sys.stdin.readline())


def readints():
    return [int(x) for x in sys.stdin.readline().split()]


T = readint()

for t in range(1, T+1):

    N = readint()

    data = []
    for _ in range(N):
        data.append(readints())

    alphas = set()

    for (a, b), (c, d) in combinations(data, 2):
        if b != d:
            alpha = frac(a-c, d-b)
            if alpha > 0:
                alphas.add(alpha)

    score = len(alphas)+1

    print("Case #{}: {}".format(t, score))
