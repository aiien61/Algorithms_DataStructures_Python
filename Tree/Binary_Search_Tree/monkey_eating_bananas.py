"""
This solution can further used to find bottlenecks in assembly lines.
"""

from math import ceil
from typing import List
import unittest

class Solution:
    def min_eating_speed(self, piles: List[int], H: int) -> int:
        """
        Find the minimum eating speed K such that monkey Koko can eat all bananas withing H hours.

        Args:
            piles: List of bananas piles where piles[i] represents bananas in pile i
            H: Maximum hours allowed to eat all bananas

        Returns:
            Minimum eating speed K, or 0 if input is invalid
        """
        if not piles:
            return 0
        
        max_banana_number: int = self._get_max(piles)
        return self._find_min_speed(piles, H, 1, max_banana_number)
    
    def _get_max(self, piles: List[int]) -> int:
        max: int = piles[0]
        for pile in piles:
            if pile > max:
                max = pile
        return max
    
    def _find_min_speed(self, piles: List[int], H: int, k_low: int, k_high: int) -> int:
        """Helper method to find minimun eating speed using binary search."""
        
        k: int = -1
        if k_high < k_low:
            return k

        k_mid: int = (k_low + k_high) // 2
        hours: int = self._calculate_hours(piles, k_mid)
        
        if hours <= H:
            k = k_mid
            k_temp = self._find_min_speed(piles, H, k_low, k_mid-1)
            if k_temp != -1:
                k = k_temp
    
        elif hours > H and k_mid < k_high:
            k = self._find_min_speed(piles, H, k_mid+1, k_high)

        return k
    
    def _calculate_hours(self, piles: List[int], k: int) -> int:
        """Calculate total hours needed to eat all piles at speed k."""
        return sum(ceil(pile / k) for pile in piles)

class TestMinEatingSpeed(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        piles: List[int] = [3, 6, 7, 11]
        H: int = 8
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 4
        self.assertEqual(actual, expected)

    def test_single_pile(self):
        piles: List[int] = [10]
        H: int = 5
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 2
        self.assertEqual(actual, expected)

    def test_exact_hours(self):
        piles: List[int] = [30, 11, 23, 4, 20]
        H: int = 5
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 30
        self.assertEqual(actual, expected)

    def test_large_numbers(self):
        piles: List[int] = [1_000_000_000]
        H: int = 2
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 500_000_000
        self.assertEqual(actual, expected)

    def test_multiple_same_piles(self):
        piles: List[int] = [5, 5, 5, 5]
        H: int = 8
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 3
        self.assertEqual(actual, expected)

    def test_long_hours(self):
        piles: List[int] = [1, 2, 3]
        H: int = 10
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 1
        self.assertEqual(actual, expected)

    def test_minimum_speed(self):
        piles: List[int] = [1, 1, 1, 1]
        H: int = 4
        actual: int = self.solution.min_eating_speed(piles, H)
        expected: int = 1
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
