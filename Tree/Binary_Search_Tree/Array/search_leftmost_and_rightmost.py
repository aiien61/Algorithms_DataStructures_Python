from typing import List
import unittest

class BST_SortedArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def search(self, value: int) -> int | None:
        """
        Regular binary search for a value in the sorted array.
        Returns the value if found, None if not found.
        """
        if not self.nums:
            return None
        
        i_start: int = 0
        i_end: int = len(self.nums) - 1
        return self._search(value, i_start, i_end)

    def _search(self, value: int, i_start: int, i_end: int):
        if i_end < i_start:
            return None

        i_mid = (i_start + i_end) // 2

        if value == self.nums[i_mid]:
            return self.nums[i_mid]
        elif value < self.nums[i_mid]:
            return self._search(value, i_start, i_mid-1)
        else:
            return self._search(value, i_mid+1, i_end)
        
    def search_leftmost(self, value: int) -> int | None:
        """
        Binary search that returns the leftmost occurrence of the value
        """
        if not self.nums:
            return None

        i_start: int = 0
        i_end: int = len(self.nums) - 1
        return self._search_leftmost(value, i_start, i_end)
        
    def _search_leftmost(self, value: int, i_start: int, i_end: int):
        if i_end < i_start:
            return None

        i_mid = (i_start + i_end) // 2

        if value == self.nums[i_mid]:
            temp = self.nums[i_mid]
            temp_left = self._search_leftmost(value, i_start, i_mid-1)
            if temp_left is not None:
                temp = temp_left
            return temp

        elif value < self.nums[i_mid]:
            return self._search_leftmost(value, i_start, i_mid-1)
        else:
            return self._search_leftmost(value, i_mid+1, i_end)
        
    def search_rightmost(self, value: int) -> int | None:
        """
        Binary search that returns the rightmost occurrence of the value
        """
        if not self.nums:
            return None

        i_start: int = 0
        i_end: int = len(self.nums) - 1
        return self._search_rightmost(value, i_start, i_end)
    
    def _search_rightmost(self, value: int, i_start: int, i_end: int):
        if i_end < i_start:
            return None

        i_mid = (i_start + i_end) // 2

        if value == self.nums[i_mid]:
            temp = self.nums[i_mid]
            temp_right = self._search_rightmost(value, i_mid+1, i_end)
            if temp_right is not None:
                temp = temp_right
            return temp

        elif value < self.nums[i_mid]:
            return self._search_rightmost(value, i_start, i_mid-1)
        else:
            return self._search_rightmost(value, i_mid+1, i_end)

class Test(unittest.TestCase):
    def test_search_when_empty(self):
        bst = BST_SortedArray(nums=[])
        actual = bst.search(2)
        expected = None
        self.assertEqual(actual, expected)

    def test_search_when_found(self):
        bst = BST_SortedArray(nums=[0, 1, 2])
        actual: int = bst.search(2)
        expected: int = 2
        self.assertEqual(actual, expected)

    def test_search_when_not_found(self):
        bst = BST_SortedArray(nums=[0, 1, 2])
        actual = bst.search(3)
        expected = None
        self.assertEqual(actual, expected)

    def test_search_leftmost_when_empty(self):
        bst = BST_SortedArray(nums=[])
        actual = bst.search_leftmost(2)
        expected = None
        self.assertEqual(actual, expected)

    def test_search_leftmost_when_found(self):
        bst = BST_SortedArray(nums=[0, 1, 1, 1, 2, 2, 2, 2])
        actual: int = bst.search_leftmost(2)
        expected: int = 2
        self.assertEqual(actual, expected)
    
    def test_search_leftmost_when_not_found(self):
        bst = BST_SortedArray(nums=[0, 1, 1, 1, 2, 2, 2, 2])
        actual = bst.search_leftmost(3)
        expected = None
        self.assertEqual(actual, expected)

    def test_search_rightmost_when_empty(self):
        bst = BST_SortedArray(nums=[])
        actual = bst.search_rightmost(2)
        expected = None
        self.assertEqual(actual, expected)

    def test_search_rightmost_when_found(self):
        bst = BST_SortedArray(nums=[0, 1, 1, 1, 2, 2, 2, 2])
        actual: int = bst.search_rightmost(2)
        expected: int = 2
        self.assertEqual(actual, expected)

    def test_search_rightmost_when_not_found(self):
        bst = BST_SortedArray(nums=[0, 1, 1, 1, 2, 2, 2, 2])
        actual = bst.search_rightmost(3)
        expected = None
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

# TODO: verify leftmost and rightmost