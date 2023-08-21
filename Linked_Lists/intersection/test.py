import unittest
from main import Solution, Singly_Linked_List


class Test(unittest.TestCase):
    sol = Solution()

    def test_intersection(self):
        llist_a = self.sol.initialize_llist([1, 2, 3, 4, 5, 6])
        llist_b = self.sol.initialize_llist([10, 11, 12])
        self.sol.generate_intersection((llist_a, 2), (llist_b, 1))
        self.assertTrue(self.sol.intersection(llist_a, llist_b))

if __name__ == "__main__":
    unittest.main()
