"""Array-based binary search tree"""
from typing import List
import unittest

class ArrayBST:
    def __init__(self, size: int):
        self.bst = [None] * size

    def insert(self, value: int) -> bool:
        """Adds a value to the BST"""
        success = self.__insert(0, value)
        return success

    def __insert(self, index: int, value: int) -> bool:
        """Helper method to recursively add a value to the BST"""
        if index >= len(self.bst):
            self.__extend_bst()

        if self.bst[index] is None:
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
        
    def __extend_bst(self) -> bool:
        """Extends the storage size of the bst """
        self.bst.extend([None] * len(self.bst))
        return True
    
    def search(self, value: int) -> int:
        """Searches for a value from the BST"""
        return self.__search(0, value)
    
    def __search(self, index: int, value: int) -> int:
        """Helper method to recursively search for a value"""
        if index >= len(self.bst) or self.bst[index] is None:
            return None
        
        if value == self.bst[index]:
            return self.bst[index]
        elif value < self.bst[index]:
            left_child_index: int = (index + 1) * 2 - 1
            return self.__search(left_child_index, value)
        else:
            right_child_index: int = (index + 1) * 2
            return self.__search(right_child_index, value)


class TestArrayBST(unittest.TestCase):
    def test_insert(self):
        bst: ArrayBST = ArrayBST(size=7)
        for value in [10, 20, 5, 7, 3, 30, 15]:
            bst.insert(value)

        expected: List[int] = [10, 5, 20, 3, 7, 15, 30]
        actual: List[int] = bst.bst
        self.assertEqual(expected, actual)

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

        expected = None
        actual = bst.search(100)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
