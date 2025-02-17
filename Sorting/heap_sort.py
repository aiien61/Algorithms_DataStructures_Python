from typing import List
import unittest
import numpy as np

class MaxHeap:
    def __init__(self):
        self.heap: List[int] = []
        self.size: int = 0

    def insert(self, num: int) -> bool:
        self.heap.append(num)

        current: int = self.size 
        while current > 0:
            parent: int = (current - 1) // 2
            if self.heap[parent] < self.heap[current]:
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
            else:
                break

        self.size += 1
        return True
    
    def pop(self) -> int:
        if self.size < 0:
            raise IndexError

        if self.size == 0:
            return None
        
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()

        max_num: int = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self._sink_down(0)
        return max_num
    
    def _sink_down(self, index: int) -> bool:
        left_child: int = (index + 1) * 2 - 1
        right_child: int = (index + 1) * 2
        max_index: int = index
        if left_child < self.size:
            if self.heap[max_index] < self.heap[left_child]:
                max_index = left_child
        
        if right_child < self.size:
            if self.heap[max_index] < self.heap[right_child]:
                max_index = right_child

        if max_index != index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            return self._sink_down(max_index)

        return True


class HeapSort:
    @staticmethod
    def sort(nums: List[int], ascend: bool):
        heap = MaxHeap()
        sorted_nums: np.ndarray = np.full(len(nums), np.nan)
        for num in nums:
            heap.insert(num)
        
        n: int = heap.size
        if ascend:
            for i in range(n):
                sorted_nums[(n - 1) - i] = heap.pop()
        else:
            for i in range(n):
                sorted_nums[i] = heap.pop()

        return sorted_nums.astype(int).tolist()


class TestHeapSort(unittest.TestCase):
    def test_ascending_sorted_list(self):
        nums: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = HeapSort.sort(nums, ascend=True)
        expected: List[int] = nums
        self.assertEqual(actual, expected)

    def test_descending_sorted_list(self):
        nums: List[int] = [5, 4, 3, 2, 1]
        actual: List[int] = HeapSort.sort(nums, ascend=False)
        expected: List[int] = nums
        self.assertEqual(actual, expected)

    def test_reverse_ascending_sorted_list(self):
        nums: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = HeapSort.sort(nums, ascend=False)
        expected: List[int] = sorted(nums, reverse=True)
        self.assertEqual(actual, expected)

    def test_reverse_descending_sorted_list(self):
        nums: List[int] = [5, 4, 3, 2, 1]
        actual: List[int] = HeapSort.sort(nums, ascend=True)
        expected: List[int] = sorted(nums)
        self.assertEqual(actual, expected)

    def test_unsorted_list_to_ascending(self):
        nums: List[int] = [66, 78, 27, 35, 6, 2, 44, 58, 29, 76]
        actual: List[int] = HeapSort.sort(nums, ascend=True)
        expected: List[int] = sorted(nums)
        self.assertEqual(actual, expected)

    def test_unsorted_list_to_descending(self):
        nums: List[int] = [66, 78, 27, 35, 6, 2, 44, 58, 29, 76]
        actual: List[int] = HeapSort.sort(nums, ascend=False)
        expected: List[int] = sorted(nums, reverse=True)
        self.assertEqual(actual, expected)

    def test_duplicate_elements(self):
        nums: List[int] = [4, 1, 3, 2, 4, 1, 3, 2]
        actual: List[int] = HeapSort.sort(nums, ascend=True)
        expected: List[int] = sorted(nums)
        self.assertEqual(actual, expected)

    def test_single_element(self):
        nums: List[int] = [10]
        actual: List[int] = HeapSort.sort(nums, ascend=True)
        expected: List[int] = sorted(nums)
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        nums: List[int] = []
        actual: List[int] = HeapSort.sort(nums, ascend=True)
        expected: List[int] = sorted(nums)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
