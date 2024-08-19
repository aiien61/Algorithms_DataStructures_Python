"""Given an undirected graph. Test if having a path between two particular nodes
"""
import unittest
from pprint import pprint
from typing import Set, Dict

class UndirectedGraph:
    def __init__(self):
        self.adjacency_list: Dict[int, list] = {}

    def neighbors(self, vertex: int) -> Set[int]:
        return set(self.adjacency_list[vertex])

    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    
    def remove_vertex(self, vertex: int) -> bool:
        if vertex not in self.adjacency_list.keys():
            return False
        
        for incident in self.adjacency_list[vertex]:
            self.adjacency_list[incident].remove(vertex)

        del self.adjacency_list[vertex]
        return True
    
    def print_graph(self) -> None:
        pprint(self.adjacency_list)


class DirectedGraph:
    def __init__(self):
        self.adjacency_list: Dict[int, list] = {}

    def neighbors(self, vertex: int) -> Set[int]:
        return set(self.adjacency_list[vertex])

    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, edge_from: int, edge_to: int) -> bool:
        if edge_from in self.adjacency_list.keys() and edge_to in self.adjacency_list.keys():
            self.adjacency_list[edge_from].append(edge_to)
            return True
        return False

    def remove_edge(self, edge_from: int, edge_to: int) -> bool:
        if edge_from in self.adjacency_list.keys() and edge_to in self.adjacency_list.keys():
            self.adjacency_list[edge_from].remove(edge_to)
            return True
        return False

    def remove_vertex(self, vertex: int) -> bool:
        for incident in self.adjacency_list.keys():
            if vertex in self.adjacency_list[incident]:
                self.adjacency_list[incident].remove(vertex)

        del self.adjacency_list[vertex]
        return True

    def print_graph(self) -> None:
        pprint(self.adjacency_list)


def dfs(graph: object, vertex: int, target: int, visited: Set[int]) -> bool:
    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            visited.add(neighbor)
            if neighbor == target:
                visited.add(neighbor)
                return True

            dfs(graph, neighbor, target, visited)
            if target in visited:
                return True
    
    return False


def has_path_between_vertices(graph: object, vertex1: int, vertex2: int) -> bool:
    visited: Set[int] = set()
    visited.add(vertex1)
    dfs(graph, vertex1, vertex2, visited)
    return vertex2 in visited


class Test(unittest.TestCase):
    def test_has_path_between_vertices_when_having_a_path_in_undirected_graph(self):
        graph: object = UndirectedGraph()
        for i in range(5):
            graph.add_vertex(i)

        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 3)
        graph.add_edge(0, 4)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)

        expected: bool = True
        actual: bool = has_path_between_vertices(graph, 2, 4)
        self.assertEqual(expected, actual)

    def test_has_path_between_vertices_when_not_having_a_path_in_undirected_graph(self):
        graph: object = UndirectedGraph()
        for i in range(5):
            graph.add_vertex(i)

        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 3)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)

        expected: bool = False
        actual: bool = has_path_between_vertices(graph, 2, 4)
        self.assertEqual(expected, actual)

    def test_has_path_between_vertices_when_having_a_path_in_directed_graph(self):
        graph: object = DirectedGraph()
        for i in range(5):
            graph.add_vertex(i)

        graph.add_edge(0, 2)
        graph.add_edge(0, 4)
        graph.add_edge(1, 0)
        graph.add_edge(2, 1)
        graph.add_edge(3, 0)
        graph.add_edge(3, 1)
        
        expected: bool = True
        actual: bool = has_path_between_vertices(graph, 2, 4)
        self.assertEqual(expected, actual)

    def test_has_path_between_vertices_when_not_having_a_path_in_directed_graph(self):
        graph: object = DirectedGraph()
        for i in range(5):
            graph.add_vertex(i)

        graph.add_edge(0, 2)
        graph.add_edge(1, 0)
        graph.add_edge(2, 1)
        graph.add_edge(3, 0)
        graph.add_edge(3, 1)

        expected: bool = False
        actual: bool = has_path_between_vertices(graph, 2, 4)
        self.assertEqual(expected, actual)
    

if __name__ == '__main__':
    unittest.main()
