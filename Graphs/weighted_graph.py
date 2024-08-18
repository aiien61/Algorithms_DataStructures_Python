"""Implement weighted graph using adjacency matrix and list
"""
import unittest
import numpy as np
import pandas as pd
from pprint import pprint
from abc import ABC, abstractmethod
from typing import Set, List
from dataclasses import dataclass


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


class Node:
    def __init__(self, name: str | int, weight: int):
        self.name: str | int = name
        self.weight: int = weight
        self.next: 'Node' = None
    
    def __repr__(self) -> str:
        return f"Node(name={self.name}, weight={self.weight})"


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def append(self, node: Node) -> bool:
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return True
        self.tail.next = node
        self.tail = node
        self.length += 1
        return True
    
    def remove(self, target: str | int) -> bool:
        if self.length == 0:
            return False
        
        if self.length == 1:
            if self.head.name == target:
                self.head = None
                self.tail = None
                self.length -= 1
                return True
            else:
                return False
        
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.name == target:
                prev.next = current.next
                current.next = None
                self.length -= 1
                return True
            
            prev = current
            current = current.next
        return False

    def has_node(self, target: str | int) -> bool:
        if self.length == 0:
            return False
        node = self.head
        while node is not None:
            if node.name == target:
                return True
            node = node.next
        return False
    
    def __repr__(self) -> str:
        result: List[Node] = []
        node = self.head
        while node is not None:
            result.append(node)
            node = node.next
        return str(result)


class WeightedAdjacencyMatrix(Graph):
    def __init__(self):
        self.adjacency_matrix = pd.DataFrame()

    @property
    def vertices(self) -> Set[int | str]:
        return set(self.adjacency_matrix.columns)
    
    def add_vertex(self, vertex: int | str) -> bool:
        if vertex not in self.adjacency_matrix.columns:
            self.adjacency_matrix[vertex] = np.inf
            self.adjacency_matrix.loc[vertex] = [np.inf] * len(self.adjacency_matrix.columns)
            self.adjacency_matrix.at[vertex, vertex] = 0
            return True
        return False
    
    def add_edge(self, vertex1: int | str, vertex2: int | str, weight: int) -> bool:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_matrix.at[vertex1, vertex2] = weight
            self.adjacency_matrix.at[vertex2, vertex1] = weight
            return True
        return False
    
    def remove_edge(self, vertex1: int | str, vertex2: int | str) -> bool:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_matrix[vertex1, vertex2] = np.inf
            self.adjacency_matrix[vertex2, vertex1] = np.inf
            return True
        return False
    
    def remove_vertex(self, vertex: int | str) -> bool:
        if vertex in self.vertices:
            self.adjacency_matrix.drop(columns=[vertex], inplace=True)
            self.adjacency_matrix.drop(index=[vertex], inplace=True)
            return True
        return False
    
    def print_graph(self) -> None:
        pprint(self.adjacency_matrix)


class WeightedAdjacencyList(Graph):
    def __init__(self):
        self.adjacency_list: dict = {}

    @property
    def vertices(self) -> Set[str | int]:
        return set(self.adjacency_list.keys())

    def add_vertex(self, vertex: str | int) -> bool:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = LinkedList()
            return True
        return False
    
    def add_edge(self, vertex1: str | int, vertex2: str | int, weight: int) -> bool:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_list[vertex1].append(Node(vertex2, weight))
            self.adjacency_list[vertex2].append(Node(vertex1, weight))
            return True
        return False
    
    def remove_edge(self, vertex1: str | int, vertex2: str | int) -> bool:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            has_edge_to_vertex2: bool = self.adjacency_list[vertex1].has_node(vertex2)
            has_edge_to_vertex1: bool = self.adjacency_list[vertex2].has_node(vertex1)
            if has_edge_to_vertex1 and has_edge_to_vertex2:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
        return False
    
    def remove_vertex(self, vertex: str | int) -> bool:
        if vertex in self.vertices:
            del self.adjacency_list[vertex]
            return True
        return False
    
    def print_graph(self) -> None:
        pprint(self.adjacency_list)


class WeightedDirectedAdjacencyMatrix(Graph):
    def __init__(self):
        self.adjacency_matrix = pd.DataFrame()

    @property
    def vertices(self) -> Set[int | str]:
        return set(self.adjacency_matrix.columns)

    def add_vertex(self, vertex: int | str) -> bool:
        if vertex not in self.adjacency_matrix.columns:
            self.adjacency_matrix[vertex] = np.inf
            self.adjacency_matrix.loc[vertex] = [np.inf] * len(self.adjacency_matrix.columns)
            self.adjacency_matrix.at[vertex, vertex] = 0
            return True
        return False

    def add_edge(self, edge_head: int | str, edge_tail: int | str, weight: int) -> bool:
        if edge_head in self.vertices and edge_tail in self.vertices:
            self.adjacency_matrix.at[edge_head, edge_tail] = weight
            return True
        return False

    def remove_edge(self, edge_head: int | str, edge_tail: int | str) -> bool:
        if edge_head in self.vertices and edge_tail in self.vertices:
            self.adjacency_matrix[edge_head, edge_tail] = np.inf
            return True
        return False

    def remove_vertex(self, vertex: int | str) -> bool:
        if vertex in self.vertices:
            self.adjacency_matrix.drop(columns=[vertex], inplace=True)
            self.adjacency_matrix.drop(index=[vertex], inplace=True)
            return True
        return False

    def print_graph(self) -> None:
        pprint(self.adjacency_matrix)


class WeightedDirectedAdjacencyList(Graph):
    def __init__(self):
        self.adjacency_list: dict = {}

    @property
    def vertices(self) -> Set[str | int]:
        return set(self.adjacency_list.keys())

    def add_vertex(self, vertex: str | int) -> bool:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = LinkedList()
            return True
        return False

    def add_edge(self, edge_head: str | int, edge_tail: str | int, weight: int) -> bool:
        if edge_head in self.vertices and edge_tail in self.vertices:
            self.adjacency_list[edge_head].append(Node(edge_tail, weight))
            return True
        return False

    def remove_edge(self, edge_head: str | int, edge_tail: str | int) -> bool:
        if edge_head in self.vertices and edge_tail in self.vertices:
            if self.adjacency_list[edge_head].has_node(edge_tail):
                self.adjacency_list[edge_head].remove(edge_tail)
                return True
        return False

    def remove_vertex(self, vertex: str | int) -> bool:
        if vertex in self.vertices:
            del self.adjacency_list[vertex]
            return True
        return False

    def print_graph(self) -> None:
        pprint(self.adjacency_list)

class Test(unittest.TestCase):
    # TODO: test weighted adjacency matrix, weighted adjacency list, weighted directed adjacency matrix, weighted directed adjacency list
    pass


if __name__ == '__main__':
    # graph: Graph = WeightedAdjacencyMatrix()
    # graph: Graph = WeightedAdjacencyList()
    # graph: Graph = WeightedDirectedAdjacencyMatrix()
    graph: Graph = WeightedDirectedAdjacencyList()
    for node in ['A', 'B', 'C', 'D', 'E']:
        graph.add_vertex(node)

    # undirected graph
    # graph.add_edge('A', 'B', 2)
    # graph.add_edge('A', 'D', 8)
    # graph.add_edge('A', 'E', 10)
    # graph.add_edge('B', 'C', 3)
    # graph.add_edge('C', 'D', 5)
    # graph.add_edge('D', 'E', 9)

    # directed graph
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('A', 'E', 3)
    graph.add_edge('B', 'C', 3)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('C', 'E', 8)
    graph.add_edge('D', 'E', 2)

    graph.print_graph()
