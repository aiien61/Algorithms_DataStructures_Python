"""Testing whether a graph is bipartite or not
"""
import logging
import unittest
from typing import List, Set
from enum import Enum, auto
from graph_class import UndirectedGraphList

logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')

class Color(Enum):
    RED = auto()
    BLACK = auto()


class Stack:
    def __init__(self):
        self.stack: List[tuple] = []
        self.length: int = 0

    def is_empty(self) -> bool:
        return True if self.length == 0 else False

    def peek(self) -> int:
        if self.length == 0:
            return None
        return self.stack[-1]
    
    def push(self, element: tuple) -> bool:
        self.stack.append(element)
        self.length += 1
        return True

    def pop(self) -> tuple:
        if self.length == 0:
            return None
        self.length -= 1
        return self.stack.pop(-1)


def is_bipartite(graph, start_vertex: int, seen: Set[int]=None, color: dict=None) -> bool:
    if color is None:
        color: dict = {
            Color.RED.name: set(),
            Color.BLACK.name: set()
        }
        
    layer: int = 0
    color[Color(layer % 2 + 1).name].add(start_vertex)
    
    if seen is None:
        seen = set()

    seen.add(start_vertex)

    to_be_colored = Stack()
    for neighbor in graph.neighbors(start_vertex):
        to_be_colored.push((neighbor, layer + 1))

    while not to_be_colored.is_empty():
        vertex, layer = to_be_colored.pop()
        if vertex in color[Color(layer % 2 + 1).name]:
            continue
        if vertex in color[Color((layer + 1) % 2 + 1).name]:
            return False
        
        color[Color(layer % 2 + 1).name].add(vertex)
        seen.add(vertex)
        for neighbor in graph.neighbors(vertex):
            to_be_colored.push((neighbor, layer + 1))

    remaining_vertices: Set[int] = graph.vertices.difference(seen)
    logging.debug(f'remaining: f{remaining_vertices}')
    if len(remaining_vertices) == 0:
        return True
    
    return is_bipartite(graph, remaining_vertices.pop(), seen, color)


class Test(unittest.TestCase):
    def test_is_bipartite_when_single_bipartite_connected_component(self):
        graph = UndirectedGraphList()
        for i in range(1, 8):
            graph.add_vertex(i)

        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(1, 5)
        graph.add_edge(1, 7)
        graph.add_edge(2, 3)
        graph.add_edge(2, 6)
        graph.add_edge(3, 5)
        graph.add_edge(3, 7)
        graph.add_edge(3, 4)
        graph.add_edge(5, 6)
        graph.add_edge(6, 7)

        expected: bool = True
        actual: bool = is_bipartite(graph, start_vertex=1)
        self.assertEqual(expected, actual)

    def test_is_bipartite_when_single_unbipartite_connected_component(self):
        graph = UndirectedGraphList()
        for i in range(1, 4):
            graph.add_vertex(i)

        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)

        expected: bool = False
        actual: bool = is_bipartite(graph, start_vertex=1)
        self.assertEqual(expected, actual)

    def test_is_bipartite_when_two_bipartite_connected_components(self):
        graph = UndirectedGraphList()
        for i in range(1, 10):
            graph.add_vertex(i)

        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(1, 5)
        graph.add_edge(1, 7)
        graph.add_edge(2, 3)
        graph.add_edge(2, 6)
        graph.add_edge(3, 5)
        graph.add_edge(3, 7)
        graph.add_edge(3, 4)
        graph.add_edge(5, 6)
        graph.add_edge(6, 7)
        graph.add_edge(8, 9)

        expected: bool = True
        actual: bool = is_bipartite(graph, start_vertex=1)
        self.assertEqual(expected, actual)

    def test_is_bipartite_when_two_connected_components_at_least_one_unbipartite(self):
        graph = UndirectedGraphList()
        for i in range(1, 11):
            graph.add_vertex(i)

        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(1, 5)
        graph.add_edge(1, 7)
        graph.add_edge(2, 3)
        graph.add_edge(2, 6)
        graph.add_edge(3, 5)
        graph.add_edge(3, 7)
        graph.add_edge(3, 4)
        graph.add_edge(5, 6)
        graph.add_edge(6, 7)
        graph.add_edge(8, 9)
        graph.add_edge(8, 10)
        graph.add_edge(9, 10)

        expected: bool = False
        actual: bool = is_bipartite(graph, start_vertex=1)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
    # graph = UndirectedGraphList()
    # for i in range(1, 10):
    #     graph.add_vertex(i)

    # graph.add_edge(1, 2)
    # graph.add_edge(1, 4)
    # graph.add_edge(1, 5)
    # graph.add_edge(1, 7)
    # graph.add_edge(2, 3)
    # graph.add_edge(2, 6)
    # graph.add_edge(3, 5)
    # graph.add_edge(3, 7)
    # graph.add_edge(3, 4)
    # graph.add_edge(5, 6)
    # graph.add_edge(6, 7)
    # graph.add_edge(8, 9)
    # graph.print_graph()

    # print(is_bipartite(graph, start_vertex=1))
