from os import system


from itertools import combinations, chain
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

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def extendg(ngraphs, subgen1, subgen2, n1, n2):

    if n1 == 0 or n2 == 0 : return -1

    nstrings = split_nlists(ngraphs)
    nosub = list()
    matrix_str = ""

    for nstring in nstrings:
        g = nlist_to_igraph(nstring)
        g.add_vertex()
        v = g.vcount() - 1

        for kset in powerset(range(0, g.vcount() - 1)):

            h = g.copy()
            for k in kset:
                h.add_edge(k, v)

            #print rednh
            if subgen1(h, n1, v): continue
            if subgen2(h.complementer(), n2, v): continue

            nosub.append(h)

    for g in nosub:
        matrix_str += list_to_matrix(g.get_adjlist()) + '\n'

    return matrix_str
