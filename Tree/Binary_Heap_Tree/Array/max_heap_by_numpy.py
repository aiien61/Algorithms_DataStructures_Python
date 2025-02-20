from typing import List
from numpy.testing import assert_array_equal
import numpy as np
import unittest
from icecream import ic

class MaxHeap:
    def __init__(self, nums: List[int]):
        self.heap: np.ndarray = np.array(nums)
        self.size: int = self.heap.size
        self._heapify()

    def _heapify(self):
        """Helper method to convert original array to binary heap tree in an array structure"""
        for i in range(self.heap.size, 0, -1):
            self._shift_up(i - 1)
        return None
    
    def _parent(self, index: int) -> int:
        """Helper method to find the index of the parent node"""
        return (index - 1) // 2
    
    def _max_child(self, index: int) -> int:
        left_child_index: int = (index + 1) * 2 - 1
        right_child_index: int = (index + 1) * 2
        max_child_index: int = index
        if left_child_index < self.size:
            if self.heap[max_child_index] < self.heap[left_child_index]:
                max_child_index = left_child_index

        if right_child_index < self.size:
            if self.heap[max_child_index] < self.heap[right_child_index]:
                max_child_index = right_child_index
        
        return max_child_index
    
    def _swap(self, index1: int, index2: int) -> None:
        """Helper method to swap values of nodes index1 and index2"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return None
    
    def _sink_down(self, index: int) -> None:
        """Helper method to sink node of index to meet heap conditions"""
        while index != self._max_child(index):
            max_child_index: int = self._max_child(index)
            self._swap(index, max_child_index)
            index = max_child_index
        return None
    
    def _bubble_up(self, index: int) -> None:
        if index <= 0:
            return None
        parent_index: int = self._parent(index)
        if self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            return self._bubble_up(parent_index)
        return None
    
    def _extend(self, heap: np.ndarray) -> np.ndarray:
        new_heap = np.full(heap.size * 2, np.nan)
        new_heap[: heap.size] = heap[:]
        return new_heap

    def insert(self, value: int) -> None:
        if self.size >= self.heap.size:
            self.heap = self._extend(self.heap)
        
        self.heap[self.size] = value
        self.size += 1
        
        current_index: int = self.size - 1
        self._bubble_up(current_index)
        return None
    
    def remove(self) -> int | None:
        if self.size == 0:
            return None
        
        max_value: int = self.heap[0]
        self.size -= 1
        if self.size > 0:
            self.heap[0] = self.heap[self.size]
            self._sink_down(0)
        return max_value
    
class TestMaxHeap(unittest.TestCase):
    def test_heapify(self):
        maxheap = MaxHeap([3, 1, 4, 1, 5, 9, 2, 6])
        actual: np.ndarray = maxheap.heap
        expected: List[int] = [9, 5, 6, 1, 3, 4, 2, 1]
        assert_array_equal(actual, expected)

    def test_insert(self):
        maxheap = MaxHeap([3, 1, 4, 1, 5, 9, 2, 6])
        maxheap.insert(10)
        self.assertEqual(maxheap.heap[0], 10)
        self.assertEqual(maxheap.size, 9)

    def test_remove(self):
        nums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
        maxheap = MaxHeap(nums)
        max_value = maxheap.remove()
        self.assertEqual(max_value, max(nums))
        self.assertEqual(maxheap.size, 7)
        self.assertNotIn(max_value, maxheap.heap)

    def test_remove_when_empty(self):
        maxheap = MaxHeap([])
        actual: np.ndarray = maxheap.heap
        expected: np.ndarray = np.array([])
        assert_array_equal(actual, expected)
        self.assertEqual(actual.size, 0)

    def test_insert_multiple(self):
        maxheap = MaxHeap([5, 3, 8])
        maxheap.insert(7)
        maxheap.insert(12)
        self.assertEqual(maxheap.heap[0], 12)
        self.assertEqual(maxheap.size, 5)
        

if __name__ == "__main__":
    unittest.main()
