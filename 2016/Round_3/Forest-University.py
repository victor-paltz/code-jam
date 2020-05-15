
import sys
from collections import defaultdict
import random
import numpy as np
#from tqdm import trange


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


def merge(lists):

    nb_lists = len(lists)
    weights = np.array([len(x) for x in lists])
    n = np.sum(weights)

    out = ""

    for size in reversed(range(n)):
        index = np.random.choice(nb_lists, 1, p=weights/(size+1))[0]
        out += lists[index].pop()
        weights[index] -= 1

    return out


# Too slow but the right solution
def generate(d, rest):

    random.shuffle(rest)
    for key in d:
        random.shuffle(d[key])
    strings = [value+[courses[key]] for key, value in d.items()]
    one_string = merge(strings+[list(rest)])
    return one_string


def generate2(d, data, index, sol):

    for key in d:
        random.shuffle(d[key])
        index[key] = -1

    np.random.shuffle(data)

    for i, x in enumerate(data):
        if x in d:
            if index[x] != -1:
                sol[i] = d[x][index[x]]
                index[x] += 1
            else:
                sol[i] = courses[int(x)]
                index[x] = 0
        else:
            sol[i] = x


T = readint()

for test in range(1, T+1):

    N = readint()
    prerequisite = readints()
    courses = readstr()
    M = readint()
    cool_words = readstr().split()

    rest = []
    d = defaultdict(list)
    for i, (pr, course) in enumerate(zip(prerequisite, courses)):
        if pr == 0:
            rest.append(i)
        else:
            d[pr-1].append(course)
    d = dict(d)

    rest = [courses[i] for i in rest if i not in d]

    # print(courses)
    # print(d)
    # print(rest)

    tot = 10**4

    sol = [0]*len(cool_words)

    #print(d, rest)

    data = np.array([str(key) for key, value in d.items()
                     for _ in range(len(value)+1)] + rest)

    d = {str(key): value for key, value in d.items()}

    index = {key: -1 for key in d}

    vec = np.zeros((N,), dtype=np.str)

    # print(data)

    for n in range(tot):

        # v1
        # one_string = generate(d, rest)

        # v2
        generate2(d, data, index, vec)

        one_string = "".join(vec)

        # print(one_string)

        for i, w in enumerate(cool_words):
            if w in one_string:
                sol[i] += 1

    res = " ".join("{:.3f}".format(float(x)/tot) for x in sol)

    print("Case #{}: {}".format(test, res))
