import unittest
from copy import deepcopy

from main import Solution, SinglyLinkedList


class Test(unittest.TestCase):
    sol = Solution()
    
    test_cases = (
        # list, k, expected
        ((10, 20, 30, 40, 50), 1, 50),
        ((10, 20, 30, 40, 50), 5, 10),
    )

    def test_return_kth_to_last_by_loop(self):
        for data, k, expected in self.test_cases:
            mylist = SinglyLinkedList(deepcopy(data))
            assert self.sol.is_valid_search(mylist, k)
            actual = self.sol.return_kth_to_last_by_loop(mylist, k)
            self.assertEqual(actual, expected)

    def test_return_kth_to_last_by_recursion(self):
        for data, k, expected in self.test_cases:
            mylist = SinglyLinkedList(deepcopy(data))
            assert self.sol.is_valid_search(mylist, k)
            actual = self.sol.return_kth_to_last_by_recursion(mylist, k)
            self.assertEqual(actual, expected)

    def test_return_kth_to_last_by_runners(self):
        for data, k, expected in self.test_cases:
            mylist = SinglyLinkedList(deepcopy(data))
            assert self.sol.is_valid_search(mylist, k)
            actual = self.sol.return_kth_to_last_by_runners(mylist, k)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
