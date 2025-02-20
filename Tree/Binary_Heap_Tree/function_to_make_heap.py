"""A function to convert a given series of random numbers into a binary max heap tree
"""
from typing import List
from icecream import ic
import unittest

class MaxHeap:
    @classmethod
    def heapify(cls, nums: List[int]) -> List[int]:
        heap: List[int] = nums[:]
        size: int = len(heap)
        i: int = size - 1
        while i >= 0:
            left: int = (i + 1) * 2 - 1
            if left >= size:
                i -= 1
                continue

            right: int = (i + 1) * 2
            if right >= size:
                if heap[i] < heap[left]:
                    heap[i], heap[left] = heap[left], heap[i]
                    i -= 1
                    continue
            
            max_i: int = i
            if heap[max_i] < heap[left]:
                max_i = left
            
            if heap[max_i] < heap[right]:
                max_i = right

            if max_i != i:
                heap[i], heap[max_i] = heap[max_i], heap[i]
                i = max_i
            else:
                i -= 1

        return heap

class TestMaxHeap(unittest.TestCase):
    def test_heapify_basic(self):
        nums = [3, 1, 4, 1, 5, 9, 2]
        heap: List[int] = MaxHeap.heapify(nums)
        self.assertTrue(self.is_max_heap(heap))

    def test_heapify_sorted(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        heap: List[int] = MaxHeap.heapify(nums)
        self.assertTrue(self.is_max_heap(heap))

    def test_heapify_reverse_sorted(self):
        nums = [7, 6, 5, 4, 3, 2, 1]
        heap: List[int] = MaxHeap.heapify(nums)
        self.assertTrue(self.is_max_heap(heap))

    def test_heapify_duplicates(self):
        nums = [1, 1, 1, 1, 1, 1, 1]
        heap: List[int] = MaxHeap.heapify(nums)
        self.assertTrue(self.is_max_heap(heap))

    def test_heapify_single_element(self):
        nums = [10]
        actual: List[int] = MaxHeap.heapify(nums)
        expected: List[int] = [10]
        self.assertEqual(actual, expected)

    def test_heapify_empty(self):
        nums = []
        actual: List[int] = MaxHeap.heapify(nums)
        expected: List[int] = []
        self.assertEqual(actual, expected)

    def is_max_heap(self, nums: List[int]) -> bool:
        size = len(nums)
        for i in range(size // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size and nums[i] < nums[left]:
                return False
            if right < size and nums[i] < nums[right]:
                return False
        return True

if __name__ == "__main__":
    unittest.main()
