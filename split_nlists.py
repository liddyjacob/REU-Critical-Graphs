"""
split_nlists.py

Split nauty adjacency lists from a file into strings.

Returns a list of strings.
"""

def split_nlists(filename):


    nlists_str = '';
    with open(filename, 'r') as nfile:
        nlists_str = nfile.read()

    gloc = 0;
    strlist = list()
    first = True

    while (gloc != -1):

        next_gloc = nlists_str.find("Graph", gloc);
        if (not first): strlist.append(nlists_str[gloc - 1 : next_gloc])
        gloc = next_gloc + 1

        if (gloc == 0): gloc = -1
        first = False

    strlist[-1]+='\n'
    return strlist;
