from igraph import Graph
from itertools import combinations
"""
subkn(g, n)

Check if g contains $K_n$

Input:
    g is an igraph.
    n is an integer.

Output:
    True if g contains kn
    False if g does not contain kn
"""

def subkn(g, n):
    return g.omega() >= n
