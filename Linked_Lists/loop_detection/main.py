import random
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

    def __iter__(self):
        seen = set()
        node = self.head
        while node:
            yield node
            if node in seen:
                break
            else:
                seen.add(node)
            node = node.next

    @property
    def data(self):
        return [node.data for node in self]
    
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

    def reform(self, llist: Singly_Linked_List, has_loop: bool) -> None:
        if not has_loop:
            return None
               
        loop_start = random.choice([node for node in llist if node.next])
        
        node = llist.head
        while node.next:
            node = node.next
        node.next = loop_start
        return None


    def detect_loop(self, llist: Singly_Linked_List) -> Union[Node, None]:
        seen = {id(llist.head)}
        node = llist.head

        def _has_seen(node: Node):
            return id(node) in seen

        while node.next and not _has_seen(node.next):
            seen.add(id(node.next))
            node = node.next

        return node.next

if __name__ == "__main__":
    sol = Solution()
    a_list = Singly_Linked_List(list('ABCDE'))
    b_list = Singly_Linked_List(list('ABCDE'))
    sol.reform(a_list, True)
    sol.reform(b_list, False)
    print(a_list.data)
    print(b_list.data)
    print(sol.detect_loop(a_list))
    print(sol.detect_loop(b_list))
    
