from typing import List
import unittest

"""In-place quick sort using pre-order traversal implementation"""
class BasicQuickSort:
    @staticmethod
    def quick_sort_inplace(unsorted_array: List[int]) -> None:
        BasicQuickSort._quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
        return None

    @staticmethod
    def _quick_sort(unsorted_array: List[int], left_i: int, right_i: int) -> None:
        if left_i >= right_i:
            return None
        
        pivot: int = BasicQuickSort._sort(unsorted_array, left_i, (left_i + right_i) // 2, right_i)

        BasicQuickSort._quick_sort(unsorted_array, left_i, pivot)
        BasicQuickSort._quick_sort(unsorted_array, pivot+1, right_i)
        return None
    
    @staticmethod
    def _sort(array: List[int], start_i: int, middle_i: int, end_i: int) -> int:
        array[middle_i], array[end_i] = array[end_i], array[middle_i]
        pivot_i: int = end_i

        left_i: int = start_i
        right_i: int = end_i - 1

        while True:
            while (left_i < right_i) and (array[left_i] <= array[pivot_i]):
                left_i += 1
            
            while (left_i < right_i) and (array[right_i] >= array[pivot_i]):
                right_i -= 1
            
            if left_i == right_i: break
            
            array[left_i], array[right_i] = array[right_i], array[left_i]
        
        if array[right_i] >= array[pivot_i]:
            array[right_i], array[pivot_i] = array[pivot_i], array[right_i]
        
        pivot_i = right_i
        return pivot_i

class BubbleQuickSort:
    @staticmethod
    def quick_sort_inplace(array: List[int]) -> None:
        low: int = 0
        high: int = len(array) - 1

        BubbleQuickSort._quick_sort(array, low, high)
        return None

    @staticmethod
    def _quick_sort(array: List[int], low=0, high=None) -> None:
        if low < high:
            pivot_i: int = BubbleQuickSort.partition(array, low, high)
            BubbleQuickSort._quick_sort(array, low, pivot_i - 1)
            BubbleQuickSort._quick_sort(array, pivot_i + 1, high)
        return None
    
    # similar with bubble sort process
    @staticmethod
    def partition(array: List[int], low: int, high: int) -> int:
        pivot: int = array[high]
        i: int = low - 1

        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

class PythonicQuickSort:
    @staticmethod
    def quick_sort(array: List[int]) -> List[int]:
        if len(array) <= 1:
            return array

        pivot: int = array[len(array) // 2]
        left: List[int] = [x for x in array if x < pivot]
        middle: List[int] = [x for x in array if x == pivot]
        right: List[int] = [x for x in array if x > pivot]
        return PythonicQuickSort.quick_sort(left) + middle + PythonicQuickSort.quick_sort(right)


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        # self.quick_sort = BasicQuickSort.quick_sort_inplace
        # self.quick_sort = BubbleQuickSort.quick_sort_inplace
        self.quick_sort = PythonicQuickSort.quick_sort
        

    def test_sorted_array(self):
        actual_array: List[int] = [1, 2, 3, 4, 5]
        expected: List[int] = [1, 2, 3, 4, 5]
        actual_array = self.quick_sort(actual_array) # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)
        

    def test_unsorted_array(self):
        actual_array: List[int] = [24, 2, 45, 20, 56, 75, 2, 56, 99, 53, 12]
        expected: List[int] = sorted([24, 2, 45, 20, 56, 75, 2, 56, 99, 53, 12])
        actual_array = self.quick_sort(actual_array)  # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)

    def test_reversed_sorted_array(self):
        actual_array: List[int] = [5, 4, 3, 2, 1]
        expected: List[int] = [1, 2, 3, 4, 5]
        actual_array = self.quick_sort(actual_array)  # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)

    def test_duplicates(self):
        actual_array: List[int] = [5, 4, 3, 3, 2]
        expected: List[int] = [2, 3, 3, 4, 5]
        actual_array = self.quick_sort(actual_array)  # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)

    def test_single_element(self):
        actual_array: List[int] = [1]
        expected: List[int] = [1]
        actual_array = self.quick_sort(actual_array)  # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)

    def test_empty_array(self):
        actual_array: List[int] = []
        expected: List[int] = []
        actual_array = self.quick_sort(actual_array)  # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)

    def test_negative_numbers(self):
        actual_array: List[int] = [-1, -3, 0, -2, 2, 1]
        expected: List[int] = [-3, -2, -1, 0, 1, 2]
        actual_array = self.quick_sort(actual_array)  # if not in-place
        # self.quick_sort(actual_array) # if in-place
        self.assertEqual(actual_array, expected)

if __name__ == '__main__':
    unittest.main()