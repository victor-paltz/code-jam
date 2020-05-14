
import sys
from collections import Counter
from math import ceil


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for t in range(1, T+1):

    N, P = readints()
    groups = [x % P for x in readints()]

    c = Counter(groups)

    nb = c[0]

    if P == 2:
        nb += int(ceil(c[1]/2))
    elif P == 3:
        nb += min(c[1], c[2])
        rest = abs(c[1]-c[2])
        nb += int(ceil(rest/3))
    elif P == 4:
        nb += c[2]//2
        nb += min(c[1], c[3])
        rest = abs(c[1]-c[3])

        if c[2] % 2 != 0:
            rest += 2

        nb += int(ceil(rest/4))
    else:
        exit()

    print("Case #{}: {}".format(t, nb))
