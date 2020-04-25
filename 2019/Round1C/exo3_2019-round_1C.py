
from functools import lru_cache


def readline_int_list():
    return [int(x) for x in input().split()]


def readline_chr():
    return input()


def readline_int():
    return int(input())


def coup_V(i1, i2, j1, j2):  # i2 and j2 excluded
    coups = []
    for j in range(j1, j2):
        if c_info[j][i2-1] <= i1:
            coups.append(j)
    return coups


def coup_H(i1, i2, j1, j2):  # i2 and j2 excluded
    coups = []
    for i in range(i1, i2):
        if r_info[i][j2-1] <= j1:
            coups.append(i)
    return coups


def mex(numbers):
    for i, v in enumerate(sorted(numbers)):
        if i != v:
            return i
    return len(numbers)


@lru_cache(None)
def nimber(i1, i2, j1, j2):

    v = coup_V(i1, i2, j1, j2)
    h = coup_H(i1, i2, j1, j2)

    if (not v and not h) or i1 >= i2 or j1 >= j2:
        return 0

    else:
        S = set()
        for i in h:
            S.add(nimber(i1, i, j1, j2) ^ nimber(i+1, i2, j1, j2))
        for j in v:
            S.add(nimber(i1, i2, j1, j) ^ nimber(i1, i2, j+1, j2))
        return mex(S)


T = int(input())

for t in range(1, T+1):
    r, c = readline_int_list()
    m = [list(readline_chr()) for _ in range(r)]

    nimber.cache_clear()

    r_info = [[0]*c for _ in range(r)]
    for i in range(r):
        r_info[i][0] = 0 if m[i][0] != "#" else 1
        for j in range(1, c):
            r_info[i][j] = r_info[i][j-1] if m[i][j] != "#" else j+1

    c_info = [[0]*r for _ in range(c)]

    for j in range(c):
        c_info[j][0] = 0 if m[0][j] != "#" else 1
        for i in range(1, r):
            c_info[j][i] = c_info[j][i-1] if m[i][j] != "#" else i+1

    v = coup_V(0, r, 0, c)
    h = coup_H(0, r, 0, c)

    tot = 0

    for i in h:
        if not (nimber(0, i, 0, c) ^ nimber(i+1, r, 0, c)):
            tot += c

    for j in v:
        if not (nimber(0, r, 0, j) ^ nimber(0, r, j+1, c)):
            tot += r

    print("Case #{}: {} {}".format(t, tot, nimber(0, r, 0, c)))
