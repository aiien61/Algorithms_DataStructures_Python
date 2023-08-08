import unittest
from main import Solution, SinglyLinkedList


class Test(unittest.TestCase):
    test_cases = (
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 5, 6, 7, 6, 5, 8, 1, 3], [0, 5, 6, 7, 8, 1, 3]),
        ([0, 0, 5, 6, 7, 6, 5, 8, 1, 8], [0, 5, 6, 7, 8, 1])
    )


    def test_remove_dups_by_set(self):
        sol = Solution()
        for data, expected in self.test_cases:
            test_list = SinglyLinkedList(data)
            sol.remove_dups_by_set(test_list)
            actual = test_list.data
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
