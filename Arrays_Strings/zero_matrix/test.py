import unittest
from main import Solution


class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ]
        )
    ]

    def test_zero_matrix(self):
        sol = Solution()
        for matrix, expected in self.test_cases:
            actual = sol.zero_matrix_by_brute_force(matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
