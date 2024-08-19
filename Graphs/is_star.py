import unittest
from graph_class import UndirectedGraphList as Graph


def is_star(graph: Graph) -> bool:
    number_of_center: int = 0
    number_of_branch: int = 0
    number_of_all_vertices: int = len(graph.vertices)
    for vertex in graph.vertices:
        if len(graph.neighbors(vertex)) == (number_of_all_vertices - 1):
            number_of_center += 1
        elif len(graph.neighbors(vertex)) == 1:
            number_of_branch += 1

    return (number_of_center == 1) and (number_of_branch == (number_of_all_vertices - 1))


class Test(unittest.TestCase):
    def test_is_star_when_star(self):
        graph: Graph = Graph()
        for vertex in range(5):
            graph.add_vertex(vertex)

        for vertex in range(1, 5):
            graph.add_edge(0, vertex)

        expected: bool = True
        actual: bool = is_star(graph)
        self.assertEqual(expected, actual)

    def test_is_star_when_not_star(self):
        graph: Graph = Graph()
        for vertex in range(5):
            graph.add_vertex(vertex)

        for vertex in range(1, 5):
            graph.add_edge(0, vertex)
        
        graph.add_edge(1, 2)

        expected: bool = False
        actual: bool = is_star(graph)
        self.assertEqual(expected, actual)
        



if __name__ == '__main__':
    unittest.main()