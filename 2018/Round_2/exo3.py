
import sys


def readint(): return int(sys.stdin.readline())


def readints(): return [int(x) for x in sys.stdin.readline().split()]


def augment(u, bigraph, visit, match):
    """augment """
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph,
                                           visit, match):
                match[v] = u       # found an augmenting path
                return True
    return False


def max_bipartite_matching(bigraph):
    """Bipartie maximum matching
    :param bigraph: adjacency list, index = vertex in U,
                                    value = neighbor list in V
    :assumption: U = V = {0, 1, 2, ..., n - 1} for n = len(bigraph)
    :returns: matching list, match[v] == u iff (u, v) in matching
    :complexity: `O(|V|*|E|)`
    """
    n = len(bigraph)               # same domain for U and V
    match = [None] * n
    for u in range(n):
        augment(u, bigraph, [False] * n, match)
    return match


T = readint()

for t in range(1, T+1):
    n = readint()

    data = []
    for _ in range(n):
        data.append(readints())

    graphs = {k: [[] for _ in range(n)] for k in range(-n, n+1) if k != 0}

    for i in range(n):
        for j in range(n):
            v = data[i][j]
            graphs[v][i].append(j)

    s = 0
    for k in range(-n, n+1):
        if k != 0:
            match = max_bipartite_matching(graphs[k])
            s += sum(1 if x is not None else 0 for x in match)

    print("Case #{}: {}".format(t, n*n-s))
