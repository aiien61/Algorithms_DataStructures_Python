"""Find all vertices reachable from rooted vertex in a connected graph
"""
import pandas as pd
from pprint import pprint
from typing import Set, List

class UndirectedGraphList:
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


class UndirectedGraphMatrix:
    def __init__(self):
        self.adjacency_matrix = pd.DataFrame()

    @property
    def num_vertices(self) -> int:
        return len(self.adjacency_matrix.axes[1])
    
    @property
    def vertices(self) -> Set[int]:
        return set(self.adjacency_matrix.columns)
    
    def neighbors(self, vertex: int) -> List[int]:
        neighbors = self.adjacency_matrix[vertex] == 1
        return self.adjacency_matrix.index[neighbors].to_list()
    
    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self.vertices:
            self.adjacency_matrix[vertex] = 0
            self.adjacency_matrix.loc[vertex] = [0] * self.num_vertices
            return True
        return False
    
    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_matrix.at[vertex1, vertex2] = 1
            self.adjacency_matrix.at[vertex2, vertex1] = 1
            return True
        return False
    
    def remove_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_matrix.at[vertex1, vertex2] = 0
            self.adjacency_matrix.at[vertex2, vertex1] = 0
            return True
        return False
    
    def remove_vertex(self, vertex: int) -> bool:
        if vertex in self.vertices:
            self.adjacency_matrix.drop(columns=[vertex], inplace=True)
            self.adjacency_matrix.drop(index=[vertex], inplace=True)
            return True
        return False
    
    def print_graph(self) -> None:
        pprint(self.adjacency_matrix)
