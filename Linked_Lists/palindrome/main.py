from typing import Union, Iterable


class Node:

    def __init__(self, data: Union[str, int]):
        self.data = data
        self.next = None


class Singly_Linked_List:

    def __init__(self, data_list: Union[str, int]):
        self.head = None
        if data_list:
            self.append(data_list)

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

    def append(self, data_list: Union[str, int]) -> None:
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

    def is_palindrome_pythonic(self, llist: Singly_Linked_List) -> bool:
        data = list(map(str, llist.data))
        s = ''.join(data)
        return s == s[::-1]
