
from collections import Counter, defaultdict


def readint():
    return int(input())


def readints():
    return [int(x) for x in input().split()]


T = int(input())

for t in range(1, T+1):

    U = readint()

    letters = set()

    data = []
    for _ in range(10000):
        q, r = input().split()
        data.append(r)
        letters = letters.union(list(r))

    c = Counter([x[0] for x in data if len(x) == U])

    p, zero = min([(c[x], x) for x in letters])

    weights = [(c[x], x) for x in letters if x != zero]
    weights.sort(reverse=True)

    res = zero + "".join(x[1] for x in weights)

    print("Case #{}: {}".format(t, res))
