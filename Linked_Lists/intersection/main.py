from typing import Iterable, Union


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.data)


class Singly_Linked_List:

    def __init__(self, data_list: Iterable):
        self.head = None
        if data_list:
            self.append_multiple(data_list)


    @property
    def data(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return result
    
    def append(self, node: Node) -> None:
        if not self.head:
            self.head = node
            return None
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = node
        return None


    def append_multiple(self, data_list: Iterable) -> None:
        index = 0
        if not self.head:
            self.head = Node(data_list[index])
            index += 1
        
        node = self.head
        while node.next:
            node = node.next
        
        for data in data_list[index:]:
            node.next = Node(data)
            node = node.next
        return None
    

class Solution:

    llist_a, llist_b = None, None

    def initialize_llist(self, data_list: Iterable) -> Singly_Linked_List:
        return Singly_Linked_List(data_list)
    
    def generate_intersection(self, llist_a: tuple, llist_b: tuple):
        """Intersect two singly linked lists. Replace data of llist_b with that
        of llist_a if the data at intersection position of both linked lists 
        are not consistent.

        Parameters:
            llist_a: a tuple of Singly_Linked_List instance and position of the
                     intersection. Position is -1 if no intersection.
            
            llist_b: a tuple of Singly_Linked_List instance and position of the
                     intersection. Position is -1 if no intersection.

        """
        if (-1 in llist_a) or (-1 in llist_b):
            return None
        
        pos_a = 0
        node_a = llist_a[0].head
        while pos_a < llist_a[-1]:
            pos_a += 1
            node_a = node_a.next
        

        if not llist_b[-1]:
            llist_b[0].head = node_a
        else:
            pos_b = 0
            node_b = llist_b[0].head
            while pos_b + 1 < llist_b[-1]:
                pos_b += 1
                node_b = node_b.next
            node_b.next = node_a
        
        return None


    # Time: O(a+b), Space: O(a)
    def intersection(self, llist_a, llist_b) -> Union[Node, None]:
        last_a, last_b = llist_a.head, llist_b.head
        a_set = {id(last_a)}
        while last_a.next or last_b.next:
            if last_a.next:
                last_a = last_a.next
                a_set.add(id(last_a))
            if last_b.next:
                last_b = last_b.next
        
        if last_a != last_b:
            return None
        
        inter = llist_b.head
        while inter:
            if id(inter) in a_set:
                return inter
            inter = inter.next
