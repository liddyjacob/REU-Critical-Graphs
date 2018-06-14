"""
list_to_matrix:

    Take an adjacency listfrom (from python)
    and turn it into a adjacency matrix string
    for nauty to process.

    Example:

    [[1], [0, 2], [1]]

    -->

    "010101010"

    (Which represents the following:
       X   0 1 2
           -----
       0 | 0 1 0
       1 | 1 0 1
       2 | 0 1 0

     1     2
      .___.
      |
      |
      .
     0                           )
"""


def list_to_matrix(adjlist):



    matrixstr = '';

    for lnode in range(0, len(adjlist)):
        rowlist = ['0',] * (len(adjlist))
        for rnode in adjlist[lnode]:

            rowlist[rnode] = '1'

        matrixstr += ''.join(rowlist)

    return matrixstr

