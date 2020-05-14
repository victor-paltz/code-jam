
import sys
from math import ceil
from collections import Counter


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for t in range(1, T+1):

    N, C, M = readints()
    P_B = readinttab(M)

    c_b = Counter(buyer for _, buyer in P_B)

    places = [p for p, _ in P_B]
    places.sort()

    # can be better -> in (log(n))
    def sk(k): return sum(1 if x <= k else 0 for x in places)

    y_min = max(int(ceil(M/N)), max(c_b.values()))

    for k in range(1, N+1):
        y_min = max(y_min, int(ceil(sk(k)/k)))

    y = y_min

    tab = [0]*(N+1)

    z = 0
    for p, b in P_B:
        if tab[p] >= y_min:
            z += 1
        else:
            tab[p] += 1

    print("Case #{}: {} {}".format(t, y, z))
