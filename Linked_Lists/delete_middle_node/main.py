from multipledispatch import dispatch
from typing import Iterable

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    
    def __init__(self, data_list: Iterable[int]):
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


    def __len__(self):
        return len(self.data)


    @dispatch(int)
    def append(self, data: int):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        return None


    @dispatch(Node)
    def append(self, new_node: Node):
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return None

    
    def append_multiple(self, data_list: Iterable[int]) -> None:
        if not isinstance(data_list, list):
            data_list = list(data_list)
        
        i = 0
        if not self.head:
            self.head = Node(data_list[i])
            i += 1
        
        node = self.head
        while node.next:
            node = node.next

        while i < len(data_list):
            node.next = Node(data_list[i])
            node = node.next
            i += 1

        return None


class Solution:

    # Time: O(1), Space: O(1)
    def delete_midnode(self, node: Node, singlylinkedlist: SinglyLinkedList):
        if not singlylinkedlist.head.next:
            return None
        
        if not singlylinkedlist.head.next.next:
            return None
        
        node.data = node.next.data
        node.next = node.next.next
        return None

    def has_node(self, node: Node, singlylinkedlist: SinglyLinkedList) -> bool:
        current = singlylinkedlist.head
        while current:
            if current.data == node.data:
                return True
            current = current.next
        return False
