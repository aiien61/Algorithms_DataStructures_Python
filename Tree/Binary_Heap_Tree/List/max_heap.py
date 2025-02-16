from dataclasses import dataclass
from typing import List
import unittest
from icecream import ic

@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None
    parent: "Node" = None


class MaxHeap:
    def __init__(self):
        self.root: Node = None
        self.tail: Node = None

    def __repr__(self):
        result: List[int] = []
        queue: List[Node] = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return str(result)

    def _shift_up(self, node: Node):
        if node.parent is None:
            return None

        if node.parent.value < node.value:
            node.parent.value, node.value = node.value, node.parent.value
            return self._shift_up(node.parent)
        
        return None
    
    def _sink_down(self, node: Node):
        max_node: int = node
        if node.left:
            if max_node.value < node.left.value:
                max_node = node.left
        
        if node.right:
            if max_node.value < node.right.value:
                max_node = node.right
        
        if max_node != node:
            node.value, max_node.value = max_node.value, node.value
            return self._sink_down(max_node)
        return None
    
    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
            return None
        
        # search left-most empty terminal using BFS
        queue: List[Node] = [self.root]
        while queue:
            size: int = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left is None:
                    new_node = Node(value)
                    new_node.parent = node
                    node.left = new_node
                    self.tail = new_node
                    queue = []
                    break
                if node.right is None:
                    new_node = Node(value)
                    new_node.parent = node
                    node.right = new_node
                    self.tail = new_node
                    queue = []
                    break
                queue.append(node.left)
                queue.append(node.right)

        self._shift_up(new_node)
        return None
    
    def pop(self) -> int:
        if self.root is None:
            return None
        
        max_value: int = self.root.value
        if self.root == self.tail:
            self.root = None
            self.tail = None
            return max_value

        self.root.value = self.tail.value
        if self.tail.parent.right == self.tail:
            self.tail = self.tail.parent.left
            self.tail.parent.right = None

        elif self.tail.parent.left == self.tail:
            node = self.tail
            
            # find split source
            while node.parent.left == node:
                node = node.parent
                if node.parent is None:
                    break
            
            # find terminal
            if node.parent is not None:
                node = node.parent.left
            
            while node.right is not None:
                node = node.right
            
            # set new tail
            self.tail.parent.left = None
            self.tail = node

        self._sink_down(self.root)
        return max_value


class TestMaxHeap(unittest.TestCase):
    def test_insert_single_element(self):
        maxheap: MaxHeap = MaxHeap()
        maxheap.insert(10)
        actual: int = maxheap.root.value
        expected: int = 10
        self.assertEqual(actual, expected)

    def test_insert_multiple_elements(self):
        maxheap: MaxHeap = MaxHeap()
        maxheap.insert(0)
        maxheap.insert(2)
        maxheap.insert(1)
        maxheap.insert(3)
        actual: List[int] = [3, 2, 1, 0]
        expected: List[int] = [3, 2, 1, 0]
        self.assertEqual(actual, expected)

    def test_insert_maintains_heap_property(self):
        values: List[int] = [10, 20, 15, 30, 25, 5]
        maxheap: MaxHeap = MaxHeap()
        for v in values:
            maxheap.insert(v)
        
        actual: int = maxheap.root.value
        expected: int = max(values)
        self.assertEqual(actual, expected)

    def test_pop_root(self):
        values: List[int] = [10, 20, 15, 30, 25, 5]
        maxheap: MaxHeap = MaxHeap()
        for v in values:
            maxheap.insert(v)

        max_value: int = maxheap.pop()
        self.assertEqual(max_value, 30)
        self.assertNotEqual(maxheap.root.value, 30)

    def test_pop_until_empty(self):
        values: List[int] = [10, 40, 30, 20, 50]
        maxheap: MaxHeap = MaxHeap()
        for v in values:
            maxheap.insert(v)

        sorted_values = sorted(values, reverse=True)
        for expected in sorted_values:
            self.assertEqual(maxheap.pop(), expected)

    def test_pop_empty_heap(self):
        maxheap: MaxHeap = MaxHeap()
        actual = maxheap.pop()
        expected = None
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()