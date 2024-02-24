import numpy as np
import unittest


class MergeSort:        
    # def __init__(self, unsorted_array: np.ndarray):
    #     self.merge_sort(unsorted_array, 0, unsorted_array.size-1)

    @classmethod
    def merge_sort(cls, unsorted_array: np.ndarray):
        cls._merge_sort(unsorted_array, 0, unsorted_array.size-1)

    @classmethod
    def _merge_sort(cls, unsorted_array: np.ndarray, index_from: int, index_to: int):
        if index_from == index_to:
            return None

        index_mid = (index_from + index_to) // 2

        cls._merge_sort(unsorted_array, index_from, index_mid)
        cls._merge_sort(unsorted_array, index_mid+1, index_to)

        cls.sort(unsorted_array, index_from, index_mid, index_to)

    @staticmethod
    def sort(unsorted_array: np.ndarray, index_from: int, index_mid: int, index_to: int):
        array_temp = np.full(unsorted_array.size, np.nan)
        
        left_index, right_index = index_from, index_mid + 1
        temp_index = index_from

        while True:
            if temp_index > index_to:
                break

            left_value, right_value = None, None

            if left_index <= index_mid:
                left_value = unsorted_array[left_index]

            if right_index <= index_to:
                right_value = unsorted_array[right_index]

            if (left_value is not None) and (right_value is not None):
                if left_value <= right_value:
                    array_temp[temp_index] = left_value
                    left_index += 1
                else:
                    array_temp[temp_index] = right_value
                    right_index += 1
            elif (left_value is None) and (right_value is not None):
                array_temp[temp_index] = right_value
                right_index += 1
            elif (left_value is not None) and (right_value is None):
                array_temp[temp_index] = left_value
                left_index += 1
            else:
                raise RuntimeError("nothing left in this interval")
            
            temp_index += 1

        unsorted_array[index_from: index_to + 1] = array_temp[index_from: index_to+1]
        return None
    

class Test(unittest.TestCase):
    test_cases = (
        np.array([5,4,3,2,1]), 
        np.array([1,2,3,4,5]), 
        np.array([5,4,3,3,3]), 
        np.array([3,3,3,2,1]), 
        np.array([24, 2, 45, 20, 56, 75, 2, 56, 99, 53, 12])
    )

    answers = (
        np.array([1,2,3,4,5]), 
        np.array([1,2,3,4,5]), 
        np.array([3,3,3,4,5]), 
        np.array([1,2,3,3,3]),
        np.array([2, 2, 12, 20, 24, 45, 53, 56, 56, 75, 99])
    )

    def test_merge_sort(self):
        for actual, expected in zip(self.test_cases, self.answers):
            MergeSort.merge_sort(actual)
            self.assertTrue(np.array_equal(actual, expected))


if __name__ == "__main__":
    unittest.main()