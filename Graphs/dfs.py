"""run dfs recursively to traverse all the vertices in a graph.
"""
from pprint import pprint
from typing import Set, List
from graph_class import UndirectedGraph

connected_component: UndirectedGraph = UndirectedGraph()
seen: Set[int] = set()

def dfs(graph: UndirectedGraph, vertex: int, R: UndirectedGraph) -> None:
    seen.add(vertex)
    for neighbor in graph.neighbors(vertex):
        if neighbor in seen:
            continue

        R.add_vertex(neighbor)
        R.add_edge(vertex, neighbor)
        dfs(graph, neighbor, R)

def main():
    graph = UndirectedGraph()
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

    graph.print_graph()

    connected_component.add_vertex(1)
    dfs(graph, 1, connected_component)
    connected_component.print_graph()


if __name__ == '__main__':
    main()
