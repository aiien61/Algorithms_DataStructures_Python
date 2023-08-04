import unittest
from copy import deepcopy

from main import Solution


class Test(unittest.TestCase):
    sol = Solution()
    
    functions = [
        sol.rotate_matrix_in_place,
        sol.rotate_matrix_by_array,
        sol.rotate_matrix_by_pythonic
    ]
    
    test_cases = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ]
        ),
        (
            [
                [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4]
            ],
            [
                [1,1,1,1],
                [2,2,2,2],
                [3,3,3,3],
                [4,4,4,4]
            ]
        )
    ]
    
    def test_matrix_rotation(self):
        for matrix, expected in self.test_cases:
            self.sol.is_legal_square_matrix(matrix)
            
            for f in self.functions:
                self.assertEqual(f(deepcopy(matrix)), expected)


if __name__ == "__main__":
    unittest.main()
