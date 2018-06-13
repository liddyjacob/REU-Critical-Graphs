from subkn import subkn
from subwn import subwn
from igraph import Graph
from unittest import TestCase
from unittest import main as test
from itertools import combinations

class TestSubG(TestCase):
    def test_empty(self):
        g = Graph()
        self.assertFalse(subkn(g, 3))
        self.assertFalse(subwn(g, 4))

    def test_k5(self):
        g = Graph()
        g.add_vertices(5)

        for pair in combinations(range(5),2):
            if pair[0] <= pair[1]:
                g.add_edges([pair])

        self.assertFalse(subkn(g, 6))
        self.assertFalse(subwn(g, 7))

        self.assertTrue(subkn(g, 3))
        self.assertTrue(subkn(g, 5))
        self.assertTrue(subwn(g, 4))

test()
