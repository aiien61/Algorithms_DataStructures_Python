from typing import List
import unittest

class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of a target value in a sorted array.

        Args:
            nums: A sorted array of integers
            target: The target value to search for
        
        Returns:
            A list of [start_index, end_index]. Returns [-1, -1] if target not found.
        """
        if not nums:
            return [-1, -1]
        return self._search_range_helper(nums, target, 0, len(nums)-1)
    
    def _search_range_helper(self, nums: List[int], target: int, i_start: int, i_end: int) -> List[int]:
        """Helper method to recursively search for the target range."""

        result: List[int] = [-1, -1]

        i_mid: int = (i_start + i_end) // 2

        if i_end < i_start:
            return result

        if target == nums[i_mid]:
            result = [i_mid, i_mid]
            left_result: List[int] = self._search_range_helper(nums, target, i_start, i_mid-1)
            if left_result[0] != -1:
                result[0] = left_result[0]

            right_result: List[int] = self._search_range_helper(nums, target, i_mid+1, i_end)
            if right_result[1] != -1:
                result[1] = right_result[1]

        elif target < nums[i_mid]:
            result = self._search_range_helper(nums, target, i_start, i_mid-1)
        else:
            result = self._search_range_helper(nums, target, i_mid+1, i_end)

        return result

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_occurrences_in_middle(self):
        nums: List[int] = [5, 7, 7, 8, 8, 10]
        target: int = 8
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [3, 4]
        self.assertEqual(actual, expected)

    def test_target_not_found(self):
        nums: List[int] = [5, 7, 7, 8, 8, 10]
        target: int = 6
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [-1, -1]
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        nums: List[int] = []
        target: int = 6
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [-1, -1]
        self.assertEqual(actual, expected)

    def test_single_element_when_target_found(self):
        nums: List[int] = [1]
        target: int = 1
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [0, 0]
        self.assertEqual(actual, expected)

    def test_single_element_when_target_not_found(self):
        nums: List[int] = [1]
        target: int = 2
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [-1, -1]
        self.assertEqual(actual, expected)

    def test_two_identical_elements(self):
        nums: List[int] = [2, 2]
        target: int = 2
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [0, 1]
        self.assertEqual(actual, expected)

    def test_multiple_consecutive_occurrences(self):
        nums: List[int] = [1, 2, 2, 2, 2, 3]
        target: int = 2
        actual: List[int] = self.solution.search_range(nums, target)
        expected: List[int] = [1, 4]
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()
