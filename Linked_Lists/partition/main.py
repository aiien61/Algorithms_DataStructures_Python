"""Partition: Write code to partition a linked list around a value x, such that 
all nodes less than x come before all nodes greater than or equal to x. 
lf x is contained within the list, the value of x only need to be after the 
elements less than x (see below). 

The partition element x can appear anywhere in the "right partition"; it does 
not need to appear between the left and right partitions.

Example:
Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from typing import Iterable


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, data_list=None):
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
    
    # Time: O(n), Space: O(1)
    def prepend(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
            return None

        node = Node(data)
        node.next = self.head
        self.head = node
        return None


    # Time: O(n), Space: O(1)
    def append(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
            return None
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(data)
        return None
    
    # Time: O(n), Space: O(n)
    def append_multiple(self, data_list: Iterable) -> None:
        i = 0
        if not self.head:
            self.head = Node(data_list[i])
            i += 1
        
        node = self.head
        while node.next:
            node = node.next
        
        for data in data_list[i: ]:
            node.next = Node(data)
            node = node.next
            i += 1
        return None


class Solution:

    # Time: O(n*n), Space: O(n)
    def partition_by_append(self, x: int, singlylinkedlist: SinglyLinkedList):
        tail = SinglyLinkedList()
        lead = SinglyLinkedList()
        
        node = singlylinkedlist.head
        while node:
            if node.data < x:
                lead.append(node.data)
            else:
                tail.append(node.data)
            node = node.next
        
        tail_node = lead.head
        while tail_node.next:
            tail_node = tail_node.next
        tail_node.next = tail.head

        return lead
    
    # Time: O(n*n), Space: O(n)
    def partition_by_prepend(self, x: int, singlylinkedlist: SinglyLinkedList):
        new_list = SinglyLinkedList()

        node = singlylinkedlist.head
        while node:
            if node.data < x:
                new_list.prepend(node.data)
            else:
                new_list.append(node.data)
            node = node.next
        return new_list
    
    # Time: O(n), Space: O(1)
    def partition(self, x: int, singlylinkedlist: SinglyLinkedList):
        current = singlylinkedlist.tail = singlylinkedlist.head

        while current:
            next_node = current.next
            current.next = None
            if current.data < x:
                current.next = singlylinkedlist.head
                singlylinkedlist.head = current
            else:
                singlylinkedlist.tail.next = current
                singlylinkedlist.tail = singlylinkedlist.tail.next
            current = next_node
        return None
    
    def is_partitioned(self, x: int, linkedlist: SinglyLinkedList) -> bool:
        is_greater_zone = False

        for node_data in linkedlist.data:
            if node_data < x:
                if is_greater_zone:
                    return False
            else:
                if not is_greater_zone:
                    is_greater_zone = True
        return True
