"""Implement Dijkstra's algorithm using min heap structure
"""
import unittest
import heapq
from pprint import pprint
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Set


class Graph(ABC):
    @abstractmethod
    def add_vertex(self) -> bool: raise NotImplementedError

    @abstractmethod
    def add_edge(self) -> bool: raise NotImplementedError

    @abstractmethod
    def remove_edge(self) -> bool: raise NotImplementedError

    @abstractmethod
    def remove_vertex(self) -> bool: raise NotImplementedError

    @abstractmethod
    def print_graph(self) -> None: raise NotImplementedError


class DirectedAcyclicGraph(Graph):
    def __init__(self):
        self.adjacency_list: Dict[str, List[tuple]] = {}

    @property
    def vertices(self) -> List[str]:
        return list(self.adjacency_list.keys())
    
    @property
    def number_of_vertices(self) -> int:
        return len(self.adjacency_list.keys())

    def get_neighbors(self, vertex: str) -> List[Tuple[str, int]]:
        if vertex not in self.adjacency_list:
            return []
        return self.adjacency_list[vertex]
    
    def get_edge(self, from_: str, to: str) -> Tuple[str, str, int] | None:
        if from_ not in self.adjacency_list:
            return None
        for edge in self.adjacency_list[from_]:
            if to == edge[0]:
                return (from_, to, edge[1])
        return None
    
    def add_vertex(self, vertex: str) -> bool:
        if not self.adjacency_list.get(vertex):
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1: str, vertex2: str, weight: int) -> bool:
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            return False
        
        self.adjacency_list[vertex1].append((vertex2, weight))
        return True
    
    def remove_edge(self, vertex1: str, vertex2: str) -> bool:
        if edges := self.adjacency_list.get(vertex1):
            for i in range(len(edges)):
                if vertex2 in edges[i]:
                    edges.pop(i)
                    return True                    
        return False
    
    def remove_vertex(self, vertex: str) -> bool:
        if vertex not in self.adjacency_list:
            return False
        
        del self.adjacency_list[vertex]
        return True
    

    def print_graph(self) -> None:
        pprint(self.adjacency_list)


class IndexedMinPQ:
    def __init__(self, size):
        self.N: int = -1
        self.size: int = size
        self.values: List[str] = [None] * size
        self.priorities: List[int] = [None] * size
        self.location: Dict[str, int] = {}

    def less(self, index1: int, index2: int) -> bool:
        return self.priorities[index1] < self.priorities[index2]
    
    def swap(self, index1: int, index2: int) -> None:
        self.values[index1], self.values[index2] = self.values[index2], self.values[index1]
        self.priorities[index1], self.priorities[index2] = self.priorities[index2], self.priorities[index1]

        self.location[self.values[index1]] = index1
        self.location[self.values[index2]] = index2
        return None
    
    def __contains__(self, value: str) -> bool:
        return value in self.location
    
    def is_empty(self) -> bool:
        return self.N < 0

    def swim(self, index: int) -> None:
        min_index: int = index
        while min_index > 0:
            if self.less(min_index, min_index // 2):
                self.swap(min_index, min_index // 2)
                min_index = min_index // 2
            else:
                break
        return None
    
    def sink(self, index: int) -> None:
        while True:
            min_index: int = index
            if (index * 2 + 1) <= self.N:
                if self.less(min_index, index * 2 + 1):
                    min_index = index * 2 + 1
            if (index * 2 + 2) <= self.N:
                if self.less(min_index, index * 2 + 2):
                    min_index = index * 2 + 2

            if min_index == index:
                break

            index = min_index
        return None
    
    def decrease_priority(self, value: str, lower_priority: int) -> None:
        index: int = self.location[value]
        if lower_priority < self.priorities[index]:
            self.priorities[index] = lower_priority
            self.swim(index)
        return None
    
    def enqueue(self, value: str, priority: int) -> bool:
        self.N += 1
        self.values[self.N], self.priorities[self.N] = value, priority
        self.location[value] = self.N
        self.swim(self.N)
        return True
    
    def dequeue(self) -> str | None:
        if self.N < 0:
            return None
        
        min_value: str = self.values[0]
        self.swap(0, self.N)
        self.values[self.N] = None
        self.priorities[self.N] = None
        self.location.pop(min_value)
        self.N -= 1
        self.sink(0)
        return min_value


def dijkstra_shortest_path(graph: DirectedAcyclicGraph, src: str) -> Dict[str, str]:
    visited: Set[str] = set()
    shortest_distance_to_src: Dict[str, int] = {v: float('inf') for v in graph.vertices}
    shortest_distance_to_src[src] = 0
    queue: List[Tuple[int, str]] = [(v, k) for k, v in shortest_distance_to_src.items()]
    node_from: Dict[str, str] = {}

    heapq.heapify(queue)
    while queue:
        distance, vertex = heapq.heappop(queue)
        visited.add(vertex)
        for neighbor, weight in graph.get_neighbors(vertex):
            if neighbor in visited:
                continue
            if distance + weight < shortest_distance_to_src[neighbor]:
                queue.remove((shortest_distance_to_src[neighbor], neighbor))
                shortest_distance_to_src[neighbor] = distance + weight
                node_from[neighbor] = vertex
                heapq.heappush(queue, (shortest_distance_to_src[neighbor], neighbor))
    return shortest_distance_to_src


class TestDijkstra(unittest.TestCase):
    def test_single_node_graph(self):
        graph = DirectedAcyclicGraph()
        graph.add_vertex('A')
        expected: Dict[str, int] = {'A': 0}
        actual: Dict[str, int] = dijkstra_shortest_path(graph, 'A')
        self.assertEqual(expected, actual)

    def test_shortest_path_when_undirected_graph_starting_from_node_A(self):
        adjacency_list = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)],
        }
        graph = DirectedAcyclicGraph()
        for vertex in adjacency_list:
            graph.add_vertex(vertex)
        for edge_from, edges in adjacency_list.items():
            for edge_to, weight in edges:
                graph.add_edge(edge_from, edge_to, weight)

        actual = dijkstra_shortest_path(graph, 'A')
        expected = {
            'A': 0,
            'B': 1,
            'C': 3,
            'D': 4,
        }
        self.assertEqual(actual, expected)

    def test_shortest_path_when_no_path(self):
        adjacency_list = {
            'A': [('B', 1)],
            'B': [('A', 1)],
            'C': [('D', 2)],
            'D': [('C', 2)],
        }
        graph = DirectedAcyclicGraph()
        for vertex in adjacency_list:
            graph.add_vertex(vertex)
        for edge_from, edges in adjacency_list.items():
            for edge_to, weight in edges:
                graph.add_edge(edge_from, edge_to, weight)

        actual = dijkstra_shortest_path(graph, 'A')
        expected = {
            'A': 0,
            'B': 1,
            'C': float('inf'),
            'D': float('inf'),
        }
        self.assertEqual(actual, expected)

    def test_shortest_path_when_unreachable_node(self):
        adjacency_list = {
            'A': [('B', 2)],
            'B': [('A', 2), ('C', 1)],
            'C': [('B', 1)],
            'D': []
        }
        graph = DirectedAcyclicGraph()
        for vertex in adjacency_list:
            graph.add_vertex(vertex)
        for edge_from, edges in adjacency_list.items():
            for edge_to, weight in edges:
                graph.add_edge(edge_from, edge_to, weight)

        actual = dijkstra_shortest_path(graph, 'A')
        expected = {
            'A': 0,
            'B': 2,
            'C': 3,
            'D': float('inf'),
        }
        self.assertEqual(actual, expected)

    def test_shortest_path_when_start_from_node_B(self):
        adjacency_list = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)],
        }
        graph = DirectedAcyclicGraph()
        for vertex in adjacency_list:
            graph.add_vertex(vertex)
        for edge_from, edges in adjacency_list.items():
            for edge_to, weight in edges:
                graph.add_edge(edge_from, edge_to, weight)

        actual = dijkstra_shortest_path(graph, 'B')
        expected = {
            'A': 1,
            'B': 0,
            'C': 2,
            'D': 3,
        }
        self.assertEqual(actual, expected)

    def test_shortest_path_when_directed_graph(self):
        dag = DirectedAcyclicGraph()
        for vertex in ['s', 'u', 'v', 'y', 'x', 'z']:
            dag.add_vertex(vertex)

        dag.add_edge('s', 'u', 1)
        dag.add_edge('s', 'x', 4)
        dag.add_edge('s', 'v', 2)
        dag.add_edge('u', 'y', 3)
        dag.add_edge('u', 'x', 1)
        dag.add_edge('x', 'y', 1)
        dag.add_edge('x', 'z', 2)
        dag.add_edge('v', 'x', 2)
        dag.add_edge('v', 'z', 3)

        actual: Dict[str, str] = dijkstra_shortest_path(dag, 's')
        expected: Dict[str, str] = {
            's': 0,
            'u': 1,
            'v': 2,
            'x': 2,
            'y': 3,
            'z': 4
        }
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
