"""Given an undirected graph, from Vs to Vd. Test if having a path from the start to the end
"""
import unittest
from typing import Set
from graph_class import UndirectedGraphList as Graph


def has_path(graph: Graph, start: str | int, end: str | int) -> bool:
    from queue import Queue

    visited: Set[str | int] = set()
    queue = Queue()
    queue.put(start)
    while not queue.empty():
        vertex: str | int = queue.get()
        if vertex not in visited:
            visited.add(vertex)
            list(map(queue.put, graph.neighbors(vertex)))
        
    return end in visited


class Test(unittest.TestCase):
    def test_has_path_when_having_a_path(self):
        graph: Graph = Graph()
        for i in range(11):
            graph.add_vertex(f'V{i}')
        
        graph.add_edge('V0', 'V1')
        graph.add_edge('V0', 'V2')
        graph.add_edge('V0', 'V3')
        graph.add_edge('V2', 'V6')
        graph.add_edge('V2', 'V7')
        graph.add_edge('V3', 'V4')
        graph.add_edge('V3', 'V5')
        graph.add_edge('V5', 'V6')
        graph.add_edge('V5', 'V8')
        graph.add_edge('V8', 'V9')
        graph.add_edge('V9', 'V10')

        expected: bool = True
        actual: bool = has_path(graph, 'V0', 'V10')
        self.assertEqual(expected, actual)

    def test_has_path_when_not_having_a_path(self):
        graph: Graph = Graph()
        for i in range(11):
            graph.add_vertex(f'V{i}')

        graph.add_edge('V0', 'V1')
        graph.add_edge('V0', 'V2')
        graph.add_edge('V0', 'V3')
        graph.add_edge('V2', 'V6')
        graph.add_edge('V2', 'V7')
        graph.add_edge('V3', 'V4')
        graph.add_edge('V3', 'V5')
        graph.add_edge('V5', 'V6')
        graph.add_edge('V5', 'V8')
        graph.add_edge('V9', 'V10')

        expected: bool = False
        actual: bool = has_path(graph, 'V0', 'V10')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()