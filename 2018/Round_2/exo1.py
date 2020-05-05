
from fractions import Fraction as frac
from itertools import combinations
import sys


def readint():
    return int(sys.stdin.readline())


def readints():
    return [int(x) for x in sys.stdin.readline().split()]


T = readint()

for t in range(1, T+1):

    C = readint()
    data = readints()

    if data[0] == 0 or data[-1] == 0:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue

    full_string = ""
    nb_lines = 0

    target = []
    for i, v in enumerate(data):
        target.extend([i]*v)

    modif = True
    while modif:

        modif = False
        target2 = list(range(C))
        s = ""
        for i, v in enumerate(target):
            if i == v:
                s += "."
            elif i < v:
                s += "\\"
                modif = True
                target2[i+1] = v
            else:
                s += "/"
                modif = True
                target2[i-1] = v

        target = target2.copy()

        full_string += s + "\n"
        nb_lines += 1

    print("Case #{}: {}".format(t, nb_lines))
    print(full_string[:-1])
