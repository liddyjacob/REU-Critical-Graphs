from igraph import GraphBase
from itertools import combinations

"""
subsn(g,n)
Check whether g contains path with n vertices
"""

def subsn(g,n):
    x = False
    for v in g.vs():
        if g.degree(v) >= n-1:
            x = True
    return x


#test cases

