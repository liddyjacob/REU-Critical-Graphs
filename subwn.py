from igraph import Graph
from itertools import combinations
"""
check_wn_on_v(g, v, n)

check if there is a wheel wn
with hub(center) v.

Input:
    g, an igraph.Graph()
    v, an igraph vertex of g
    n, an integer.

Output:
    True if there is a wheel on v
    False if there is not a wheel
on v.

"""
def check_wn_on_v(g, v, n):
    neighbors = g.neighbors(v)
    tire_g = g.induced_subgraph(neighbors)
    #NOW CHECK FOR CYCLE OF LENGTH N IN TIRE!




"""
subpn(g, n)

Check if g contains $W_n$

Input:
    g is an igraph.
    n is an integer.

Output:
    True if g contains Wn
    False if g does not contain Wn
"""

def subwn(g, n):

    found = False

    for v in g.vs():
        if g.degree(v) >= n:
            found = check_wn_on_v(g, v, n)

        if found: return True

    return False

