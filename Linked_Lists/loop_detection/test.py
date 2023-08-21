import unittest
from main import Solution, Singly_Linked_List


class Test(unittest.TestCase):

    sol = Solution()
    test_cases = [[list('ABCDE'), True],
                  [list('ABCDE'), False]]

    def test_loop_detection(self):
        for data, expected in self.test_cases:
            llist = Singly_Linked_List(data)
            self.sol.reform(llist, expected)
            print(llist.data, end=' ')
            actual = self.sol.detect_loop(llist)
            print(actual)
            self.assertEqual(bool(actual), expected)


if __name__ == "__main__":
    unittest.main()
