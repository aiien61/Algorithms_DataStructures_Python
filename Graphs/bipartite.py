"""Testing whether a graph is bipartite or not
"""
import unittest
from typing import List, Set
from enum import Enum, auto
from graph_class import UndirectedGraphList

class Color(Enum):
    RED = auto()
    BLACK = auto()

color: dict = {
    Color.RED.name: set(),
    Color.BLACK.name: set()
}

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
    
# TODO: test
def is_bipartite(graph, start_vertex: int, seen: Set[int]=None) -> bool:
    layer: int = 0
    color[Color(layer % 2 + 1).name].add(start_vertex)
    to_be_colored = Stack()
    if seen is None:
        seen = {start_vertex}

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
    if len(remaining_vertices) == 0:
        return True
    
    return is_bipartite(graph, remaining_vertices.pop(), seen)


class Test(unittest.TestCase):
    def test_is_bipartite(self):
        pass
