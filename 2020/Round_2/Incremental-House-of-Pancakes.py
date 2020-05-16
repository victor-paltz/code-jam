
import sys
from math import floor


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


def trinome(a, b, c):
    d = b*b - 4*a*c
    return .5*(-b+d**.5)


T = readint()

for test in range(1, T+1):

    L, R = readints()

    n = 0

    diff = abs(L-R)

    n1 = int(floor(trinome(1, 1, -2*diff) + 1e-20))

    if n1*(n1+1)//2 > diff:
        n1 -= 1

    if L >= R:
        n += n1
        L -= n*(n+1)//2
    else:
        n += n1
        R -= n*(n+1)//2

    rev = False

    if L < R:
        L, R = R, L
        rev = True

    n += 1

    x = trinome(1, n+1, n-L)
    y = trinome(1, n+2, n-R)

    if x < 0:
        x = -1
    else:
        x = int(floor(x + 1e-10))

    if y < 0:
        y = -1
    else:
        y = int(floor(y + 1e-10))

    x += 3
    y += 3

    dl = (n+x)*(x+1)
    dr = (n+1+x)*(y+1)

    while dl > L:
        x -= 1
        dl = (n+x)*(x+1)

    while dr > R:
        y -= 1
        dr = (n+1+x)*(y+1)

    y = min(x, y)

    dl = (n+x)*(x+1)
    dr = (n+1+y)*(y+1)

    L -= round(dl)
    R -= round(dr)

    n += x+y+1

    L = int(L)
    R = int(R)
    n = int(n)

    if rev:
        L, R = R, L

    print("Case #{}: {} {} {}".format(test, n, L, R))
