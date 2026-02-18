class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True
    
    def remove(self, value) -> Node | None:
        if self.length == 0:
            return None
        
        if self.head.value == value and self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        if self.head.value == value:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp
        
        if self.tail.value == value:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            
            self.tail = temp
            temp = temp.next
            self.tail.next = None
            self.length -= 1
            return temp
        
        prev = self.head
        while prev.next != None:
            if prev.next.value == value:
                break
            prev = prev.next
        
        if prev.next is None:
            return None
        
        temp = prev.next
        prev.next = prev.next.next
        temp.next = None
        self.length -= 1
        return temp


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def print_graph(self):
        for node in self.adjacency_list:
            adjacent_nodes = []
            adjacency = self.adjacency_list[node]
            if adjacency.length != 0:
                adjacent_node = adjacency.head
                while adjacent_node:
                    adjacent_nodes.append(adjacent_node.value)
                    adjacent_node = adjacent_node.next
            
            print(f"{node}: {adjacent_nodes}")
    
    def add_node(self, node: Node) -> bool:
        if node not in self.adjacency_list:
            self.adjacency_list[node.value] = LinkedList()
            return True
        return False
    
    def add_edge(self, node1: Node, node2: Node) -> bool:
        if node1.value in self.adjacency_list and node2.value in self.adjacency_list:
            self.adjacency_list[node1.value].append(node2.value)
            self.adjacency_list[node2.value].append(node1.value)
            return True
        return False
    
    def remove_edge(self, node1: Node, node2: Node) -> bool:
        if node1.value in self.adjacency_list and node2.value in self.adjacency_list:
            self.adjacency_list[node1.value].remove(node2.value)
            self.adjacency_list[node2.value].remove(node1.value)
            return True
        return False
    
    def remove_node(self, node: Node) -> bool:
        if node.value not in self.adjacency_list:
            return False
        
        other_node = self.adjacency_list[node.value].head
        while other_node is not None:
            self.adjacency_list[other_node.value].remove(node.value)
            other_node = other_node.next
        del self.adjacency_list[node.value]
        return True
    
if __name__ == "__main__":
    v1 = Node(1)
    v2 = Node(2)
    v3 = Node(3)
    v4 = Node(4)
    v5 = Node(5)

    g = Graph()
    g.add_node(v1)
    g.add_node(v2)
    g.add_node(v3)
    g.add_node(v4)
    g.add_node(v5)
    
    g.add_edge(v1, v2)
    g.add_edge(v1, v3)
    g.add_edge(v3, v4)

    g.print_graph()

    print("--- after remove_edge(v1, v3) ---")

    g.remove_edge(v3, v4)
    g.print_graph()

    print("--- after remove_node(v3) ---")
    g.remove_node(v3)
    g.print_graph()
