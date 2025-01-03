"""Array-based binary search tree"""
from icecream import ic
import numpy as np
import unittest

class ArrayBST:
    def __init__(self, size: int):
        self.bst: np.ndarray = np.full(size, np.nan)
    
    def insert(self, value: int) -> bool:
        success: bool = self.__insert(0, value)
        return success
    
    def __insert(self, index: int, value: int) -> bool:
        if index >= len(self.bst):
            extra: np.ndarray = np.full(self.bst.size, np.nan)
            self.bst = np.concatenate((self.bst, extra))

        if np.isnan(self.bst[index]):
            self.bst[index] = value
            return True
        
        if value == self.bst[index]:
            print(f"Node {value} already exists. Can't insert")
            return False
        elif value < self.bst[index]:
            left_child_index: int = (index + 1) * 2 - 1
            return self.__insert(left_child_index, value)
        else:
            right_child_index: int = (index + 1) * 2
            return self.__insert(right_child_index, value)
    
    def search(self, value: int) -> int:
        return self.__search(0, value)
    
    def __search(self, index: int, value: int) -> int:
        if index >= self.bst.size or np.isnan(self.bst[index]):
            return np.nan
        
        if value == self.bst[index]:
            return self.bst[index]
        elif value < self.bst[index]:
            left_child_index: int = (index + 1) * 2 - 1
            return self.__search(left_child_index, value)
        else:
            right_child_index: int = (index + 1) * 2
            return self.__search(right_child_index, value)
        
class TestArrayBST(unittest.TestCase):
    def test_insertion(self):
        bst: ArrayBST = ArrayBST(size=7)
        for value in [10, 20, 5, 7, 3, 30, 15]:
            bst.insert(value)

        expected: np.ndarray = np.array([10, 5, 20, 3, 7, 15, 30])
        actual: np.ndarray = bst.bst
        np.testing.assert_array_equal(expected, actual)

    def test_search_when_found(self):
        bst: ArrayBST = ArrayBST(size=7)
        for value in [10, 20, 5, 7, 3, 30, 15]:
            bst.insert(value)

        expected: int = 30
        actual: int = bst.search(30)
        self.assertEqual(expected, actual)

    def test_search_when_not_found(self):
        bst: ArrayBST = ArrayBST(size=7)
        for value in [10, 20, 5, 7, 3, 30, 15]:
            bst.insert(value)

        expected = np.nan
        actual = bst.search(100)
        np.testing.assert_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
