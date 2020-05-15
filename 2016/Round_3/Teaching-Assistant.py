
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    seq = readstr()

    cum = 0
    pile = []

    for x in seq:
        if pile:
            prev = pile.pop()
            if prev == x:
                cum += 10
            else:
                pile.append(prev)
                pile.append(x)
        else:
            pile.append(x)

    sol = cum + 5*len(pile)//2

    print("Case #{}: {}".format(test, sol))
