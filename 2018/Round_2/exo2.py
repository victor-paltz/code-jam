
import sys


def readint(): return int(sys.stdin.readline())


def readints(): return [int(x) for x in sys.stdin.readline().split()]


def sac_a_dos(R, B, tab):
    n = len(tab)
    f = [[0]*(B+1) for _ in range(R+2)]

    for i in range(n):
        for r in reversed(range(R+1)):
            for b in reversed(range(B+1)):
                ri, bi = tab[i]
                if r >= ri and b >= bi:
                    f[r][b] = max(1+f[r-ri][b-bi], f[r][b])

    return f


def solve(R, B):

    if R > B:
        R, B = B, R

    elts = []
    for n in range(1, min(B+1, 33)):
        for i in range(min(n, R)+1):
            elts.append((i, n-i))

    sol = sac_a_dos(R, B, elts)

    return sol


T = readint()

sol_big = solve(500, 500)

for t in range(1, T+1):

    R, B = readints()

    if R > B:
        R, B = B, R

    sol = 0

    if min(R, B) > 32:
        sol = sol_big[R][B]
    else:
        sol = solve(R, B)[R][B]

    print("Case #{}: {}".format(t, sol))
