from igraph import GraphBase
from itertools import combinations

"""
subpn(g,n)
Check whether g contains path with n vertices
"""

def subpn(g,n):
	if len(g.path_length_hist()[0])>=n:
		return True
	else:
		return False


