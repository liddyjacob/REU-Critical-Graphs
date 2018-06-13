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

#test cases
g = GraphBase()
g.add_vertices(4)
g.add_edges([(0,1),(0,2),(0,3)])
print(subpn(g,3) )
print(subpn(g,2) )
#print (g.path_length_hist()[0])
