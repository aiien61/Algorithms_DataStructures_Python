import unittest
from typing import Tuple

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def _parent(self, index: int) -> int:
        return index // 2
    
    def _max_child(self, index: int) -> int:
        left_child: int = (index + 1) * 2 - 1
        right_child: int = (index + 1) * 2
        max_child: int = index

        if left_child < self.size:
            if self.heap[max_child] < self.heap[left_child]:
                max_child = left_child
        
        if right_child < self.size:
            if self.heap[max_child] < self.heap[right_child]:
                max_child = right_child
        
        return max_child

    
    def _swap(self, index1: int, index2: int) -> bool:
        bound: int = self.size - 1
        if index1 < 0 or bound < index1:
            return False
        
        if index2 < 0 or bound < index2:
            return False
        
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]
        return True
    
    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.size += 1
        current: int = self.size - 1
        while current > 0:
            parent_index: int = self._parent(current)
            if self.heap[parent_index] < self.heap[current]:
                self._swap(parent_index, current)
            current = parent_index
        return None
    
    def remove(self) -> int | None:
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            self.size -= 1
            return self.heap.pop()
        
        max_value: int = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self._sink_down(0)
        return max_value
    
    def _sink_down(self, index: int) -> None:
        while index != self._max_child(index):
            max_child_index: int = self._max_child(index)
            self._swap(index, max_child_index)
            index = max_child_index
        return None


class TestMaxHeap(unittest.TestCase):
    def test_insert(self):
        maxheap = MaxHeap()
        maxheap.insert(1)
        maxheap.insert(0)
        maxheap.insert(3)
        maxheap.insert(2)
        actual: int = maxheap.heap[0]
        expected: int = 3
        self.assertEqual(actual, expected)

    def test_remove(self):
        maxheap = MaxHeap()
        maxheap.insert(1)
        maxheap.insert(0)
        maxheap.insert(3)
        maxheap.insert(2)
        actual: Tuple[int] = maxheap.remove(), maxheap.heap[0]
        expected: Tuple[int] = (3, 2)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
