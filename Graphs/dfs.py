"""run dfs recursively to traverse all the vertices in a graph.
"""
from enum import Enum, auto
from pprint import pprint
from typing import Set, List
from graph_class import UndirectedGraphList, UndirectedGraphMatrix


class GraphType(Enum):
    LIST = auto()
    MATRIX = auto()


def make_graph(graph):
    for i in range(1, 9):
        graph.add_vertex(i)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(3, 7)
    graph.add_edge(3, 8)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(7, 8)

    return graph


def traversal_by_dfs(by: GraphType):
    graph = UndirectedGraphList() if by == GraphType.LIST else UndirectedGraphMatrix()
    R = UndirectedGraphList() if by == GraphType.LIST else UndirectedGraphMatrix()
    seen: Set[int] = set()

    def dfs(graph, vertex, R) -> None:
        seen.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor in seen:
                continue
            
            R.add_vertex(neighbor)
            R.add_edge(vertex, neighbor)
            dfs(graph, neighbor, R)

    graph = make_graph(graph)
    graph.print_graph()

    R.add_vertex(1)
    dfs(graph, 1, R)
    R.print_graph()


if __name__ == '__main__':
    traversal_by_dfs(by=GraphType.MATRIX)
