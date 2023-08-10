from typing import Iterable


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, data_list: Iterable[int]):
        self.head = None
        if data_list:
            self.append_multiple(data_list)

    @property
    def data(self):
        node = self.head
        data_list = []
        while node is not None:
            data_list.append(node.data)
            node = node.next
        return data_list
    
    def __len__(self):
        return len(self.data)

    def append_multiple(self, data_list: Iterable[int]):
        if not isinstance(data_list, list):
            data_list = list(data_list)

        if not self.head:
            self.head = Node(data_list.pop(0))

        current = self.head
        while current.next is not None:
            current = current.next
        for data in data_list:
            current.next = Node(data)
            current = current.next
        return None


class Solution:

    def is_valid_search(self, singlylinkedlist, k) -> bool:
        return False if k > len(singlylinkedlist) else True


    # Time: O(n), Space: O(1)
    def return_kth_to_last_by_loop(self, singlylinkedlist, k) -> int:
        j = len(singlylinkedlist) - k
        i = 0
        node = singlylinkedlist.head
        while i < j:
            node = node.next
            i += 1
        return node.data


    # Time: O(n), Space: O(1)
    def return_kth_to_last_by_recursion(self, singlylinkedlist, k) -> int:
        if len(singlylinkedlist) - k > 0:
            singlylinkedlist.head = singlylinkedlist.head.next
            return self.return_kth_to_last_by_recursion(singlylinkedlist, k)
        else:
            return singlylinkedlist.head.data
        
    # Time: O(n), Space: O(1)
    def return_kth_to_last_by_runners(self, singlylinkedlist, k) -> int:
        p1 = singlylinkedlist.head
        p2 = singlylinkedlist.head
        for _ in range(k):
            p1 = p1.next
        
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2.data
