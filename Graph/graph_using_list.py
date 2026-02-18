import unittest

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except KeyError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return False
        
        for other_vertex in self.adjacency_list[vertex]:
            self.adjacency_list[other_vertex].remove(vertex)
        del self.adjacency_list[vertex]
        return True


    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")


class TestGraph(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        expected = {
            'A': [],
            'B': [],
            'C': []
        }
        self.assertEqual(g.adjacency_list, expected)

    def test_add_edge(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        g.add_edge('A', 'B')
        g.add_edge('C', 'A')

        expected = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A']
        }
        self.assertEqual(g.adjacency_list, expected)


    def test_remove_edge(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')

        g.remove_edge('A', 'C')

        expected = {
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B']
        }
        self.assertEqual(g.adjacency_list, expected)

        """
            EXPECTED OUTPUT:
            ----------------
            Graph before remove_edge():
            A : ['B', 'C']
            B : ['A', 'C']
            C : ['B', 'A']

            Graph after remove_edge(A, C):
            A : ['B']
            B : ['A', 'C']
            C : ['B']
        """

    def test_remove_vertex(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('A', 'D')
        g.add_edge('B', 'D')
        g.add_edge('C', 'D')

        g.remove_vertex('D')

        expected = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A']
        }

        self.assertEqual(g.adjacency_list, expected)

        """
            EXPECTED OUTPUT:
            ----------------
            Graph before remove_vertex():
            A : ['B', 'C', 'D']
            B : ['A', 'D']
            C : ['A', 'D']
            D : ['A', 'B', 'C']

            Graph after remove_vertex(D):
            A : ['B', 'C']
            B : ['A']
            C : ['A']

        """


if __name__ == "__main__":
    unittest.main()
