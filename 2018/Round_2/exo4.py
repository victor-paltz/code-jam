
import sys

import numpy as np
from collections import Counter

from scipy.ndimage.measurements import label


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def neighbours(i, j, n, m):
    if i > 0:
        yield i-1, j
    if i < n-1:
        yield i+1, j
    if j > 0:
        yield i, j-1
    if j < m-1:
        yield i, j+1


def connected_components(mat, value):
    n = len(mat)
    m = len(mat[0])
    mark = [[0 for j in range(m)] for i in range(n)]
    mark_counter = 0

    seen = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == value and not mark[i][j]:
                mark_counter += 1
                queue = [(i, j)]
                while queue:
                    i1, j1 = queue.pop()
                    seen.add((i1, j1))
                    if mat[i1][j1] == value and not mark[i1][j1]:
                        mark[i1][j1] = mark_counter
                        queue.extend(x for x in neighbours(
                            i1, j1, n, m) if x not in seen)
    return mark


def connected_components2(mat, value):
    structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    comp, _ = label(data2 == value, structure)
    return comp


def get_patterns(data):

    rules = set()

    s = np.sum(data)

    if s != 0:
        rules.add((1, 1, 1, 1))
    if s != R*C:
        rules.add((0, 0, 0, 0))

    stop = False
    for i in range(R):
        for j in range(C-1):
            if np.all(data[i, j:j+2] == np.array([0, 1])):
                rules.add((0, 1, 0, 1))
                stop = True
                break
        if stop:
            break

    stop = False
    for i in range(R):
        for j in range(C-1):
            if np.all(data[i, j:j+2] == np.array([1, 0])):
                rules.add((1, 0, 1, 0))
                stop = True
                break
        if stop:
            break

    stop = False
    for i in range(R-1):
        for j in range(C):
            if np.all(data[i:i+2, j] == np.array([1, 0])):
                rules.add((1, 1, 0, 0))
                stop = True
                break
        if stop:
            break

    stop = False
    for i in range(R-1):
        for j in range(C):
            if np.all(data[i:i+2, j] == np.array([0, 1])):
                rules.add((0, 0, 1, 1))
                stop = True
                break
        if stop:
            break

    stop = False
    for i in range(R-1):
        for j in range(C-1):
            arr = data[i:i+2, j:j+2]
            rules.add(tuple(arr.flatten()))

    return list(rules)


T = readint()

for t in range(1, T+1):
    R, C = readints()

    data = []
    for _ in range(R):
        data.append([1 if x == "B" else 0 for x in readstr()])

    data = np.array(data)

    rules = get_patterns(data)

    best = 0

    for i in range(R+1):
        for j in range(C+1):
            for rule in rules:
                data2 = data.copy()
                data2[:i, :j] = data[:i, :j] == rule[0]
                data2[:i, j:] = data[:i, j:] == rule[1]
                data2[i:, :j] = data[i:, :j] == rule[2]
                data2[i:, j:] = data[i:, j:] == rule[3]

                if np.count_nonzero(data2) <= best:
                    continue

                #comp = connected_components(data2, True)
                comp = connected_components2(data2, True)

                c = Counter(x for lin in comp for x in lin)
                c[0] = -1

                best = max(best, max(c.values()))

    print("Case #{}: {}".format(t, best))
