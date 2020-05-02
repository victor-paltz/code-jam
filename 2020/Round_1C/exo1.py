
from collections import Counter, defaultdict


def readint():
    return int(input())


def readints():
    return [int(x) for x in input().split()]


T = readint()

for t in range(1, T+1):

    X, Y, PATH = input().split()

    X = int(X)
    Y = int(Y)

    ok = False

    for i, direction in enumerate(PATH):
        if direction == "N":
            Y += 1
        elif direction == "S":
            Y -= 1
        elif direction == "E":
            X += 1
        elif direction == "W":
            X -= 1
        else:
            exit()

        if abs(X) + abs(Y) <= i+1:
            ok = True
            print("Case #{}: {}".format(t, i+1))
            break

    if not ok:
        print("Case #{}: IMPOSSIBLE".format(t))
