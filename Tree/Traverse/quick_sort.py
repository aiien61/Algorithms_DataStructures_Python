import numpy as np
import unittest


class QuickSort:
    def __init__(self, values: np.ndarray):
        self.quick_sort(values, 0, values.size-1)

    def quick_sort(self, values: np.ndarray, left_index: int, right_index: int):
        if values.size == 0:
            return None
        
        if left_index == right_index:
            return None
        
        if (left_index > right_index):
            return None
        
        pivot_i_temp = self.get_pivot_index(left_index, right_index)
        pivot_i = self.sort(values, left_index, pivot_i_temp, right_index)
        
        self.quick_sort(values, left_index, pivot_i-1)
        self.quick_sort(values, pivot_i+1, right_index)
        return None
    
    def get_pivot_index(self, left_index: int, right_index: int) -> int:
        return (left_index + right_index) // 2
    
    def sort(self, values: np.ndarray, start_index: int, pivot_index: int, end_index: int) -> int:
        values[pivot_index], values[end_index] = values[end_index], values[pivot_index]
        pivot_index = end_index
        pivot = values[pivot_index]
        left_index, right_index = start_index, end_index - 1

        while True:

            while True:
                if left_index == right_index:
                    break
                if pivot < values[left_index]:
                    break
                left_index += 1

            while True:
                if right_index == left_index:
                    break
                if values[right_index] < pivot:
                    break
                right_index -= 1
            
            if left_index == right_index:
                break

            values[left_index], values[right_index] = values[right_index], values[left_index]
        
        if values[pivot_index] < values[left_index]:
            values[pivot_index], values[left_index] = values[left_index], values[pivot_index]

        return left_index


class Test(unittest.TestCase):
    test_cases = [
        (np.array([5, 4, 3, 2, 1]), np.array([1, 2, 3, 4, 5])),
        (np.array([20, 10, 50, 30, 70, 60, 40]), np.array([10, 20, 30, 40, 50, 60, 70])),
        (np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4, 5]))
    ]
    def test_quick_sort(self):
        for actual, expected in self.test_cases:
            quick_sort = QuickSort(actual)
            result = np.array_equal(actual, expected)
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

    

        