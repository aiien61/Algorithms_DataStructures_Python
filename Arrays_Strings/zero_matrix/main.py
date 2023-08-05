class Solution:
    def zero_matrix_by_brute_force(self, matrix: list):
        """If any element in the matrix is zero, set all elements in the same 
        column and row to zero.
        """

        m = len(matrix)
        n = len(matrix[0])
        row_map = [0] * m
        col_map = [0] * n

        # locate and store the coordinates of all the target elements
        for x in range(m * n):
            row, col = divmod(x, m)
            if matrix[row][col] == 0:
                row_map[row] = 1
                col_map[col] = 1

        # replace to zero
        for x in range(m * n):
            row, col = divmod(x, m)
            if row_map[row] or col_map[col]:
                matrix[row][col] = 0
        return matrix
