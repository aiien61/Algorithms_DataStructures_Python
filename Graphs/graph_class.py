"""Find all vertices reachable from rooted vertex in a connected graph
"""
from pprint import pprint
from typing import Set, List
from queue import Queue

class UndirectedGraph:
    def __init__(self):
        self.adjacency_list: dict = {}
    
    @property
    def vertices(self) -> Set[int]:
        return set([vertex for vertex in self.adjacency_list])
    
    def neighbors(self, vertex: int) -> List[int]:
        return self.adjacency_list[vertex]
    
    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex: int) -> bool:
        if vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    def print_graph(self) -> None:
        pprint(self.adjacency_list)
