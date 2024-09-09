"""Implement binary search using divide & conquer approach

Given a sorted list of n distinct integers, and integer x

Find j if x equals some integer of index j
"""
import unittest
import math
from typing import List

def binary_search(x: int, sorted_array: List[int], n: int) -> int:
    """Binary search to locate the index of the target integer in the sorted array recursively.

    Args:
      x [int]: an integer to be search in the array
      sorted_array [list]: a list of sorted integers
      n [int]: the length of the sorted array

    Returns:
      The index of x in the array 
    """
    if n <= 0:
        return -1 

    mid: int = math.ceil((n - 1) / 2)
    if x == sorted_array[mid]:
        return mid
    elif x < sorted_array[mid]:
        found: int = binary_search(x, sorted_array[: mid], mid)
        return found
    elif x > sorted_array[mid]:
        found: int = binary_search(x, sorted_array[mid + 1:], n - mid - 1)
        return found if found < 0 else mid + found + 1


class TestBinarySearch(unittest.TestCase):
    def test_odd_array_when_found_in_middle(self):
        arr = [1, 3, 5, 7, 9]
        expected: int = 2
        actual: int = binary_search(5, arr, 5)
        self.assertEqual(expected, actual)

    def test_odd_array_when_found_in_first(self):
        arr = [1, 3, 5, 7, 9]
        expected: int = 0
        actual: int = binary_search(1, arr, 5)
        self.assertEqual(expected, actual)

    def test_odd_array_when_found_in_last(self):
        arr = [1, 3, 5, 7, 9]
        expected: int = 4
        actual: int = binary_search(9, arr, 5)
        self.assertEqual(expected, actual)

    def test_even_array_when_found_in_middle(self):
        arr = [1, 3, 5, 7, 9, 11]
        expected: int = 2
        actual: int = binary_search(5, arr, 6)
        self.assertEqual(expected, actual)

        expected = 3
        actual = binary_search(7, arr, 6)
        self.assertEqual(expected, actual)

    def test_even_array_when_found_in_first(self):
        arr = [1, 3, 5, 7, 9, 11]
        expected: int = 0
        actual: int = binary_search(1, arr, 6)
        self.assertEqual(expected, actual)

    def test_even_array_when_found_in_last(self):
        arr = [1, 3, 5, 7, 9, 11]
        expected: int = 5
        actual: int = binary_search(11, arr, 6)
        self.assertEqual(expected, actual)

    def test_binary_search_when_not_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        expected: int = -1
        actual: int = binary_search(2, arr, 6)
        self.assertEqual(expected, actual)

    def test_binary_search_when_found_out_of_range(self):
        arr = [1, 3, 5, 7, 9, 11]
        expected: int = -1
        actual: int = binary_search(12, arr, 6)
        self.assertEqual(expected, actual)

    def test_binary_search_when_empty_array(self):
        arr = []
        expected: int = -1
        actual: int = binary_search(5, arr, 0)
        self.assertEqual(expected, actual)

    def test_binary_search_when_single_element_found(self):
        arr = [7]
        expected: int = 0
        actual: int = binary_search(7, arr, 1)
        self.assertEqual(expected, actual)

    def test_single_elementarray_when_not_found(self):
        arr = [7]
        expected: int = -1
        actual: int = binary_search(1, arr, 1)
        self.assertEqual(expected, actual)

    def test_binary_search_when_found_in_middle_in_large_sorted_array(self):
        arr = list(range(1, 100001))
        expected: int = 49_999
        actual: int = binary_search(50_000, arr, 100_000)
        self.assertEqual(expected, actual)

    def test_binary_search_when_found_in_last_in_large_sorted_array(self):
        arr = list(range(1, 100001))
        expected: int = 99_999
        actual: int = binary_search(100_000, arr, 100_000)
        self.assertEqual(expected, actual)
    
    def test_binary_search_when_found_in_first_in_large_sorted_array(self):
        arr = list(range(1, 100001))
        expected: int = 0
        actual: int = binary_search(1, arr, 100_000)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
