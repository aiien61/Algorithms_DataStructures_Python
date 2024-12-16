from typing import List
from icecream import ic
import unittest

ic.disable()

class MergeSort:
    @staticmethod
    def merge_sort(array: List[int]) -> None:
        low: int = 0
        high: int = len(array)-1
        ic('start: ', array, low, high)
        MergeSort._merge_sort(array, low, high)

    @staticmethod
    def _merge_sort(array: List[int], low: int, high: int) -> None:
        ic('break: ', low, high)
        if low >= high:
            return None
        
        mid: int = (low + high) // 2

        MergeSort._merge_sort(array, low, mid)
        MergeSort._merge_sort(array, mid+1, high)

        MergeSort._merge(array, low, mid, high)
        return None

    @staticmethod
    def _merge(array: List[int], low: int, mid: int, high: int) -> None:
        ic('merge:', low, mid, high)
        temp_array: List[int] = [None] * len(array)

        left: int = low
        right: int = mid + 1
        temp_index: int = low

        # merge the two halves into temp[]
        while left <= mid and right <= high:
            ic(left, mid, right, high)
            if array[left] <= array[right]:
                temp_array[temp_index] = array[left]
                left += 1
            else:
                temp_array[temp_index] = array[right]
                right += 1
            temp_index += 1

        # copy remanining elements from the left half
        while left <= mid:
            ic(left, mid)
            temp_array[temp_index] = array[left]
            left += 1
            temp_index += 1

        # copy remaining elements from the right half
        while right <= high:
            ic(right, high)
            temp_array[temp_index] = array[right]
            right += 1
            temp_index += 1
        
        for i in range(low, high + 1):
            array[i] = temp_array[i]
        
        return None

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.merge_sort = MergeSort.merge_sort

    def test_sorted_array(self):
        actual: List[int] = list(range(1, 6))
        expected: List[int] = list(range(1, 6))
        self.merge_sort(actual)
        self.assertEqual(actual, expected)

    def test_unsorted_array(self):
        actual: List[int] = [20, 1, 2, 5, 3, 15, 16, 10, 23, 0, 8, 9, 18]
        expected: List[int] = sorted(actual)
        self.merge_sort(actual)
        self.assertEqual(actual, expected)

    def test_reversed_array(self):
        actual: List[int] = [5, 4, 3, 2, 1]
        expected: List[int] = [1, 2, 3, 4, 5]
        self.merge_sort(actual)
        self.assertEqual(actual, expected)
    
    def test_array_with_duplicates(self):
        actual: List[int] = [5, 4, 3, 3, 2]
        expected: List[int] = [2, 3, 3, 4, 5]
        self.merge_sort(actual)
        self.assertEqual(actual, expected)

    def test_single_element(self):
        actual: List[int] = [1]
        expected: List[int] = [1]
        self.merge_sort(actual)
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        actual: List[None] = []
        expected: List[None] = []
        self.merge_sort(actual)
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        actual: List[int] = [-1, -2, -3, 0, -2, 2, 1]
        expected: List[int] = sorted(actual)
        self.merge_sort(actual)
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()