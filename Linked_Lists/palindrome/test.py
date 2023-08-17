import unittest
from main import Solution, Singly_Linked_List


class Test(unittest.TestCase):
    sol = Solution()
    test_cases = [("level", True),
                  ("leve1", False),
                  ("aa", True),
                  ("aba", True),
                  ([1, 2, 3, 4, 3, 2, 1], True),
                  ([1], True),
                  (["a", "a"], True),
                  ([], True),
                  ([1, 2, 3, 4, 5], False),
                  ([1, 2], False)]

    def test_is_palindrome(self):
        for test_case, expected in self.test_cases:
            llist = Singly_Linked_List(test_case)
            self.assertEqual(self.sol.is_palindrome_pythonic(llist), expected)
