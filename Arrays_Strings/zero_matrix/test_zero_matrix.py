import unittest
from copy import deepcopy


def zero_matrix_by_brute_force(matrix: list) -> list:
    m = len(matrix)
    n = len(matrix[0])

    zero_position = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                zero_position.append((i, j))
                
    for row, col in zero_position:
        for i in range(m):
            matrix[i][col] = 0

        for j in range(n):
            matrix[row][j] = 0
    
    return matrix


def zero_matrix(matrix: list) -> list:
    m = len(matrix)
    n = len(matrix[0])
    row_has_zero, col_has_zero = False, False
    
    for j in range(n):
        if matrix[0][j] == 0:
            row_has_zero = True
            break
            
    for i in range(m):
        if matrix[i][0] == 0:
            col_has_zero = True
            break
            
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    
    for i in range(m):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)
            
    for j in range(n):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)
            
    if row_has_zero:
        nullify_row(matrix, 0)
        
    if col_has_zero:
        nullify_column(matrix, 0)
    
    return matrix


def nullify_row(matrix: list, row: int) -> None:
    for j in range(len(matrix[row])):
        matrix[row][j] = 0
    return None


def nullify_column(matrix: list, column: int) -> None:
    for i in range(len(matrix)):
        matrix[i][column] = 0
    return None


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

    test_functions = [
        zero_matrix_by_brute_force,
        zero_matrix
    ]

    def test_zm(self):
        for f in self.test_functions:
            for test_matrix, expected in self.test_cases:
                matrix = deepcopy(test_matrix)
                self.assertEqual(f(matrix), expected)

if __name__ == "__main__":
    unittest.main()
