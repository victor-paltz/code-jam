
from fractions import Fraction as frac
from itertools import combinations
import sys
from math import ceil, floor


def readint():
    return int(sys.stdin.readline())


def readints():
    return [int(x) for x in sys.stdin.readline().split()]


def get_j(c, alpha_min, alpha_max):
    j = int(alpha_min*c)
    while j <= alpha_min*c:
        j += 1
    return j


T = readint()

for t in range(1, T+1):

    N = readint()

    data = []
    for _ in range(N):
        data.append(readints())

    alpha_min, alpha_max = frac(0, 1), frac(int(1e10), 1)

    ok = True

    for (a, b), (c, d) in combinations(data, 2):
        if (b == d and a > c) or (a == c and b > d):
            ok = False
            break
        if b != d and a != c:
            alpha = frac(a-c, d-b)
            if alpha < 0:
                if a > c:
                    ok = False
                    break
            else:
                if a > c:
                    alpha_min = max(alpha_min, alpha)
                else:
                    alpha_max = min(alpha_max, alpha)

    if not ok or alpha_max <= alpha_min:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    #print(alpha_min, alpha_max)

    int_part = int(floor(alpha_min))

    alpha_min -= int_part
    alpha_max -= int_part

    alpha_mean = alpha_min+(alpha_max-alpha_min)/2

    N_left, N_right = 1, int(1e10)

    while N_left != N_right:

        N = N_left + (N_right-N_left)//2

        f = alpha_mean.limit_denominator(N)
        j = f.numerator
        c = f.denominator

        if alpha_min*c < j < alpha_max*c:
            N_right = min(N_right-1, N)
        else:
            N_left = max(N_left+1, N)

    c = N_left
    j = get_j(c, alpha_min, alpha_max)

    if not alpha_min*c < j < alpha_max*c:
        c = N_left+1
        j = get_j(c, alpha_min, alpha_max)

    if not alpha_min*c < j < alpha_max*c:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    print("Case #{}: {} {}".format(t, c, j+c*int_part))
