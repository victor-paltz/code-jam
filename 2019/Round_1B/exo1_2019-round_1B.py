
import numpy as np

T = int(input())


def cumsum(data):
    res = []
    s = 0
    for x in data:
        s += x
        res.append(s)
    return res


def read_int_array():
    return [int(x) for x in input().split()]


for t in range(1, T+1):

    x0, y0 = 0, 0

    couples = dict((orr, []) for orr in "NSEW")
    P, Q = read_int_array()
    for _ in range(P):
        x, y, direction = input().split()
        couples[direction].append((int(x), int(y)))

    # case y

    rank_N = np.array([0]*(Q+1))
    rank_S = np.array([0]*(Q+1))

    for (x, y) in couples["N"]:
        rank_N[y+1] += 1
    for (x, y) in couples["S"]:
        rank_S[y-1] += 1

    cumsum_N = np.cumsum(rank_N)
    cumsum_S = np.cumsum(rank_S[::-1])[::-1]

    total = cumsum_N + cumsum_S

    y0 = np.argmax(total)

    # case x

    rank_E = np.array([0]*(Q+1))
    rank_W = np.array([0]*(Q+1))

    for (x, y) in couples["E"]:
        rank_E[x+1] += 1
    for (x, y) in couples["W"]:
        rank_W[x-1] += 1

    cumsum_E = np.cumsum(rank_E)
    cumsum_W = np.cumsum(rank_W[::-1])[::-1]

    total = cumsum_E + cumsum_W

    x0 = np.argmax(total)

    print("Case #{}: {} {}".format(t, x0, y0))
