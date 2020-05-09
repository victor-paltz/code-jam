
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


T = readint()

for test in range(1, T+1):

    D, N = readints()
    k_s = []
    for _ in range(N):
        k_s.append(readints())

    t = max((D-k)/s for k, s in k_s)

    sol = D/t

    print("Case #{}: {:.6f}".format(test, sol))
