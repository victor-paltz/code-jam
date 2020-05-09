
import sys
from heapq import *
import numpy as np
#from fractions import Fraction as frac


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def floyd_warshall2(weight):
    """All pairs shortest paths by Floyd-Warshall.
    An improved implementation by Pascal-Ortiz
    :param weight: edge weight matrix
    :modifies: weight matrix to contain distances in graph
    :returns: True if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    for k, Wk in enumerate(weight):
        for _, Wu in enumerate(weight):
            for v, Wuv in enumerate(Wu):
                alt = Wu[k] + Wk[v]
                if alt < Wuv:
                    Wu[v] = alt
    for v, Wv in enumerate(weight):
        if Wv[v] < 0:      # negative cycle found
            return True
    return False


def dijkstra(graph, weight, source=0, target=None):
    """single source shortest paths by Dijkstra
       :param graph: directed graph in listlist or listdict format
       :param weight: in matrix format or same listdict graph
       :assumes: weights are non-negative
       :param source: source vertex
       :type source: int
       :param target: if given, stops once distance to target found
       :type target: int
       :returns: distance table, precedence table
       :complexity: `O(|V| + |E|log|V|)`
    """
    n = len(graph)
    assert all(weight[u][v] >= 0 for u in range(n) for v in graph[u])
    prec = [None] * n
    black = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)       # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for neighbor in graph[node]:
                dist_neighbor = dist_node + weight[node][neighbor]
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec


T = readint()

for test in range(1, T+1):

    N, Q = readints()

    E_S = []
    for _ in range(N):
        E_S.append(readints())

    adj = []
    for _ in range(N):
        adj.append([x if x != -1 else float("inf") for x in readints()])

    targets = []
    for _ in range(Q):
        targets.append(readints())

    if False:
        # version 1
        graph = [[j for j in range(N) if adj[i][j] != float("inf")]
                 for i in range(N)]
        final_adj = []
        for i, (e, s) in enumerate(E_S):
            final_adj.append([x/s if x <= e else float("inf")
                              for x in dijkstra(graph, adj, i)[0]])
    else:
        # version 2
        floyd_warshall2(adj)
        final_adj = adj.copy()
        for i, (e, s) in enumerate(E_S):
            for j in range(N):
                final_adj[i][j] = adj[i][j] / \
                    s if adj[i][j] <= e else float("inf")

    ok = floyd_warshall2(final_adj)

    res = [final_adj[start-1][end-1] for start, end in targets]

    output = " ".join("{:.8f}".format(x) for x in res)

    print("Case #{}: {}".format(test, output))
