from os import system

from igraph import Graph
from nlist_to_igraph import nlist_to_igraph
from split_nlists import split_nlists
from list_to_matrix import list_to_matrix

"""
filter.py

Filter graphs of a certain type.

Input is:
    g6graphs: nauty graphs in ./showg form.
    subgeneric: function for filter
** NOTE THAT THERE ARE ALSO COMMAND LINE FLAGS **

Output is nauty graphs in g6 form, filtering
graphs that contain specified subgraphs.
"""


def filterg(ngraphs, subgeneric, n):

    if n == 0: return -1

    nstrings = split_nlists(ngraphs)
    nosub = list()
    matrix_str = ""

    for nstring in nstrings:
        g = nlist_to_igraph(nstring)
        # Check to see if subgraph is there.
        if not subgeneric(g, n): nosub.append(g)

    for g in nosub:
        matrix_str += list_to_matrix(g.get_adjlist()) + '\n'

    return matrix_str
