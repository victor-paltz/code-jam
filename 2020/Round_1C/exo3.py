
from fractions import Fraction as frac
from math import floor
import sys


def readint():
    return int(sys.stdin.readline())


def readints():
    return [int(x) for x in sys.stdin.readline().split()]


T = readint()

for t in range(1, T+1):

    N, D = readints()
    angles = sorted(readints())

    tot_angle = sum(angles)

    slices = [frac(a, c) for c in range(1, D+1)
              for a in angles if D*a <= tot_angle*c]

    slices = sorted(set(slices))

    best = 1

    for a in slices:

        if sum(floor(ang/a) for ang in angles) < D:
            continue

        tab = [floor(ang/a) for ang in angles if floor(ang/a)*a == ang]

        amount = 0
        total = 0
        for v in tab:
            if total + v > D:
                break
            total += v
            amount += 1

        best = max(best, amount)

    print("Case #{}: {}".format(t, D-best))
