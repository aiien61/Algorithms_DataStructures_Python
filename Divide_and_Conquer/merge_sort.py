"""Implement Merge Sort on linked list using divide & conquer, DFS, and post-order approaches
"""
import unittest
import logging
import random
from typing import List

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class Node:
    def __init__(self, value: int, next=None):
        self.value: int = value
        self.next: 'Node' = next

    def __repr__(self) -> str:
        result: List[str] = []
        node = self
        while node is not None:
            result.append(f'Node({node.value})')
            node = node.next
        return ' -> '.join(result)



def merge_sort(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    def get_middle(node: Node) -> Node:
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def merge(left: Node, right: Node):
        dummy: Node = Node(float('inf'))
        tail: Node = dummy
        while left and right:
            if left.value < right.value:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        
        if left:
            tail.next = left
        
        if right:
            tail.next = right

        return dummy.next
                
    middle: Node = get_middle(head)
    right_head: Node = middle.next
    middle.next = None

    sorted_left: Node = merge_sort(head)
    sorted_right: Node = merge_sort(right_head)

    return merge(sorted_left, sorted_right)


def list_to_linkedlist(elements: List[int]) -> Node:
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head

def linkedlist_to_list(head: Node) -> List[int]:
    result: List[int] = []
    while head:
        result.append(head.value)
        head = head.next
    return result


class TestMergeSortLinkedList(unittest.TestCase):
    def test_when_given_sorted_list(self):
        linked_list = list_to_linkedlist([1, 2, 3, 4, 5])
        sorted_list = merge_sort(linked_list)
        expected: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = linkedlist_to_list(sorted_list)
        self.assertEqual(expected, actual)

    def test_when_given_unsorted_list(self):
        linked_list = list_to_linkedlist([4, 2, 5, 1, 3])
        sorted_list = merge_sort(linked_list)
        expected: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = linkedlist_to_list(sorted_list)
        self.assertEqual(expected, actual)

    def test_when_empty_list(self):
        linked_list = list_to_linkedlist([])
        sorted_list = merge_sort(linked_list)
        expected: List[int] = []
        actual: List[int] = linkedlist_to_list(sorted_list)
        self.assertEqual(expected, actual)

    def test_when_single_element_list(self):
        linked_list = list_to_linkedlist([42])
        sorted_list = merge_sort(linked_list)
        expected: List[int] = [42]
        actual: List[int] = linkedlist_to_list(sorted_list)
        self.assertEqual(expected, actual)

    def test_when_duplicates_elements(self):
        linked_list = list_to_linkedlist([3, 1, 10, 3, 2])
        sorted_list = merge_sort(linked_list)
        expected: List[int] = [1, 2, 3, 3, 10]
        actual: List[int] = linkedlist_to_list(sorted_list)
        self.assertEqual(expected, actual)

    def test_when_large_list(self):
        random.seed(100)
        random_numbers: List[int] = [random.randint(1, 1000) for _ in range(1000)]
        linked_list = list_to_linkedlist(random_numbers)
        sorted_list = merge_sort(linked_list)
        expected: List[int] = sorted(random_numbers)
        actual: List[int] = linkedlist_to_list(sorted_list)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
