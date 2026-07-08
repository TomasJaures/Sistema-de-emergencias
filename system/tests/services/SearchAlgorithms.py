import unittest
import sys
import os
## Para importar de otras carpetas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from services.SearchAlgorithms import SearchAlgorithm
from structures.Graphs.Graph import Graph
from structures.Graphs.Node import Node


class TestDijkstra(unittest.TestCase):

    def setUp(self):

        self.graph = Graph()

        self.a = Node("A")
        self.b = Node("B")
        self.c = Node("C")
        self.d = Node("D")
        self.e = Node("E")
        self.f = Node("F")
        self.g = Node("G")
        self.h = Node("H")
        self.i = Node("I")
        self.j = Node("J")
        self.k = Node("K")
        self.l = Node("L")
        self.m = Node("M")
        self.n = Node("N")
        self.o = Node("O")
        self.p = Node("P")

        self.nodes = [
            self.a,self.b,self.c,self.d,
            self.e,self.f,self.g,self.h,
            self.i,self.j,self.k,self.l,
            self.m,self.n,self.o,self.p
        ]

        self.graph.addNodes(self.nodes)


        self.graph.addEdge(self.a, self.b, 4, addressed=True)
        self.graph.addEdge(self.b, self.c, 2, addressed=True)
        self.graph.addEdge(self.b, self.d, 3, addressed=True)
        self.graph.addEdge(self.c, self.a, 4, addressed=True)

        self.graph.addEdge(self.g, self.c, 6, addressed=True)
        self.graph.addEdge(self.c, self.i, 5, addressed=True)
        self.graph.addEdge(self.i, self.c, 7, addressed=True)

        self.graph.addEdge(self.l, self.i, 4, addressed=True)
        self.graph.addEdge(self.i, self.l, 5, addressed=True)
        self.graph.addEdge(self.h, self.i, 4, addressed=True)

        self.graph.addEdge(self.d, self.e, 4, addressed=True)
        self.graph.addEdge(self.e, self.d, 5, addressed=True)
        self.graph.addEdge(self.e, self.f, 1, addressed=True)
        self.graph.addEdge(self.e, self.g, 7, addressed=True)
        self.graph.addEdge(self.e, self.c, 8, addressed=True)

        self.graph.addEdge(self.g, self.e, 6, addressed=True)
        self.graph.addEdge(self.g, self.h, 1, addressed=True)

        self.graph.addEdge(self.f, self.j, 5, addressed=True)
        self.graph.addEdge(self.g, self.j, 3, addressed=True)

        self.graph.addEdge(self.j, self.k, 2, addressed=True)

        self.graph.addEdge(self.k, self.l, 7, addressed=True)

        self.graph.addEdge(self.l, self.n, 2, addressed=True)
        self.graph.addEdge(self.l, self.m, 6, addressed=True)

        self.graph.addEdge(self.m, self.n, 6, addressed=True)

        self.graph.addEdge(self.n, self.o, 4, addressed=True)
        self.graph.addEdge(self.o, self.p, 4, addressed=True)
        self.graph.addEdge(self.p, self.n, 5, addressed=True)
        self.graph.addEdge(self.p, self.k, 10, addressed=True)




    def test_shortest_path_A_to_P(self):

        result = SearchAlgorithm.dijkstra(
            self.a,
            lambda node: node.data == "P"
        )

        target, path, visited, weight = result


        self.assertEqual(target.data, "P")

        self.assertEqual([node.data for node in path],["A", "B", "C", "I", "L", "N", "O", "P"])

        self.assertEqual(weight, 26)


    def test_shortest_path_A_to_C(self):

        result = SearchAlgorithm.dijkstra(
            self.a,
            lambda node: node.data == "C"
        )


        target, path, visited, weight = result


        self.assertEqual(target.data, "C")

        self.assertEqual(
            [node.data for node in path],
            ["A", "B", "C"]
        )

        self.assertEqual(weight, 6)


    def test_condition_with_multiple_targets(self):

        # Existen varios nodos que podrian cumplir
        # La condicion busca el primero encontrado por menor costo

        result = SearchAlgorithm.dijkstra(
            self.a,
            lambda node: node.data in ["E", "J"]
        )


        target, path, visited, weight = result


        self.assertEqual(target.data, "E")

        self.assertEqual(
            [node.data for node in path],
            ["A", "B", "D", "E"]
        )

        self.assertEqual(weight, 11)
    
    def test_dijkstra_multiple_execution_same_graph(self):
        result1 = SearchAlgorithm.dijkstra(self.a,lambda node: node.data == "P")
        target1, path1, visited1, weight1 = result1
        result2 = SearchAlgorithm.dijkstra(self.a, lambda node: node.data == "C")

        target2, path2, visited2, weight2 = result2

        # Primera busqueda
        self.assertEqual(target1.data, "P")
        self.assertEqual( [node.data for node in path1], ["A", "B", "C", "I", "L", "N", "O", "P"])
        self.assertEqual(weight1, 26)

        # Segunda busqueda (mismos objetos Node)
        self.assertEqual(target2.data, "C")
        self.assertEqual([node.data for node in path2], ["A", "B", "C"] )
        self.assertEqual(weight2, 6)

    def test_node_not_found(self):

        result = SearchAlgorithm.dijkstra(
            self.a,
            lambda node: node.data == "Z"
        )

        self.assertIsNone(result)



if __name__ == "__main__":
    unittest.main()