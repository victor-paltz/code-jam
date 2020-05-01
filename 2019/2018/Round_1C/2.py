
from collections import Counter, defaultdict


def readline():
    return [int(x) for x in input().split()]


T = int(input())

for t in range(1, T+1):

    N = readline()[0]

    pref = [0]*N
    given = [False]*N
    tot = 0

    for _ in range(N):

        array = readline()

        parf = array[1:]

        if array[0] == -1:
            exit()

        for p in parf:
            pref[p] += 1

        possibles = [(pref[p], p) for p in parf if not given[p]]

        if possibles:
            _, p_give = min(possibles)
            given[p_give] = True
            print(p_give, flush=True)
        else:
            print(-1, flush=True)
