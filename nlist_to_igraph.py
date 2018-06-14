from sys import exit
from igraph import Graph


"""
nlist_to_igraph

Turn a nauty adjacency list into an igraph.

Input will be string.

Output will be igraph.
"""

def strlist_to_list(strlist):
    pass

def nlist_to_igraph(nliststr):

    order_pos = nliststr.find("order");
    if (order_pos == -1):
        print "In nlist_to_igraph: INPUT DOES NOT LIST ORDER";
        exit(-1)

    order_pos = order_pos + len("order ")
    endline_pos = nliststr.find('.')

    order = int(nliststr[order_pos:endline_pos])

    g = Graph()
    g.add_vertices(order)

    nliststr = nliststr[order_pos : -1]
    lists = nliststr.split("\n");

    for i in range(1, len(lists)):
        node = i - 1;
        lstr = lists[i]
        col_pos = lstr.find(':')
        vertex_str = lstr[col_pos + 2 : -1]

        if (vertex_str == ""): continue

        vertices = vertex_str.split(' ');
        vertices = map(int, vertices);

        for v in vertices:
            if (v > node): g.add_edge(node, v )


    return g
