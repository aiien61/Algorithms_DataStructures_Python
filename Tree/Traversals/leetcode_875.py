"""
Link: https://leetcode.com/problems/koko-eating-bananas/description/
"""

import unittest
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        
        i_low = 0
        i_high = 10 ** 9
        return self._find_min_speed(piles, h, i_low, i_high)

    def _find_min_speed(self, piles, h, i_low, i_high) -> int:
        if i_high < i_low:
            return -1

        i_mid = (i_low + i_high) // 2
        hours_taken = self.calculate_hours(piles, i_mid)
        
        if hours_taken <= h:
            result = i_mid
            result_tmp = self._find_min_speed(piles, h, i_low, i_mid-1)
            if result_tmp != -1:
                result = result_tmp

        elif hours_taken > h:
            result = self._find_min_speed(piles, h, i_mid+1, i_high)

        return result
    
    @staticmethod
    def calculate_hours(piles, speed) -> int:
        total_hours = 0
        for pile in piles:
            hours, leftover = divmod(pile, speed)
            if leftover:
                hours += 1
            total_hours += hours
        return total_hours
    

class Test(unittest.TestCase):
    piles = {
        4: ([3, 6, 7, 11], 8),
        30: ([30, 11, 23, 4, 20], 5),
        23: ([30, 11, 23, 4, 20], 6)
    }
    def test_minEatingSpeed(self):
        for expected, arguments in self.piles.items():
            piles, h = arguments
            actual = Solution().minEatingSpeed(piles, h)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
