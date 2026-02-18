"""Run BFS to traverse all the vertices in a graph.
"""
from enum import Enum, auto
from queue import Queue
from typing import Set, List
from graph_class import UndirectedGraphList, UndirectedGraphMatrix

class GraphType(Enum):
    LIST = auto()
    MATRIX = auto()

def make_graph(graph):
    for i in range(1, 14):
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
    graph.add_edge(9, 10)
    graph.add_edge(11, 12)
    graph.add_edge(12, 13)

    return graph

def bfs(graph, to_be_visited, R, seen) -> None:
    while not to_be_visited.empty():
        head, tail = to_be_visited.get()
        if tail in seen:
            continue

        seen.add(tail)
        R.add_vertex(tail)
        R.add_edge(head, tail)

        for neighbor in graph.neighbors(tail):
            to_be_visited.put((tail, neighbor))

    R.print_graph()


def find_all_connected_components(graph, by) -> None:
    vertices_visited: Set[int] = set()
    while graph.vertices.difference(vertices_visited):
        left_vertices: Set[int] = graph.vertices.difference(vertices_visited)
        start_vertex: int = left_vertices.pop()
        queue: Queue = Queue()
        R = UndirectedGraphList() if by == GraphType.LIST else UndirectedGraphMatrix()
        R.add_vertex(start_vertex)

        vertices_visited.add(start_vertex)
        for neighbor in graph.neighbors(start_vertex):
            queue.put((start_vertex, neighbor))

        bfs(graph, queue, R, vertices_visited)


def traversal_by_bfs(by: GraphType):
    graph = UndirectedGraphList() if by == GraphType.LIST else UndirectedGraphMatrix()
    graph = make_graph(graph)
    graph.print_graph()

    find_all_connected_components(graph, by)


if __name__ == '__main__':
    traversal_by_bfs(by=GraphType.MATRIX)
