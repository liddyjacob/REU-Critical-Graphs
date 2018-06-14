from igraph import Graph
from itertools import combinations
from subkn import subkn

def is_path(g, (v1, v2), n, path = None):


    if len(path) == 1:
        path.append(v1)
        path.append(v2)

    if n == 1:
        return v2 in g.neighbors(v1)

    for k in g.neighbors(v1):

        if k in path: continue

        if is_path(g, (k, v2), n - 1, path + [k,]): return True

    return False

def subcn(g, n):
    if n == 2: return subkn(g, 2)
    if n == 3: return subkn(g, 3)

    for v in g.vs():

        if (g.degree(v) < 2): continue

        neighbors = g.neighbors(v)

        for pair in combinations(neighbors, 2):
            if is_path(g, pair, n - 2, [v.index,]): return True


    return False
