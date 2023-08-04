class Solution:

    def is_legal_square_matrix(self, matrix: list) -> bool:
        n = len(matrix)
        assert n > 0, "illegal matrix"

        warning = "It's not allowed to rotate non-square matrix"
        for row_index in range(n):
            assert len(matrix[row_index]) == n, warning
        
        return True


    def rotate_matrix_in_place(self, matrix: list) -> list:
        """Rotates a matrix 90 degrees clockwise in place"""
        n = len(matrix)

        for layer in range(n // 2):
            first, last = layer, n - layer - 1
            for i in range(first, last):
                # save top
                top = matrix[layer][i]

                # left -> top
                matrix[layer][i] = matrix[-i-1][layer]

                # bottom -> left
                matrix[-i-1][layer] = matrix[-layer-1][-i-1]

                # right -> bottom
                matrix[-layer-1][-i-1] = matrix[i][-layer-1]

                # top -> right
                matrix[i][-layer-1] = top
        return matrix


    def rotate_matrix_by_array(self, matrix: list) -> list:
        n = len(matrix)
        
        new_matrix = [[0] * n for _ in range(n)]
        for j, layer in enumerate(matrix[::-1]):
            for i, entry in enumerate(layer):
                new_matrix[i][j] = entry

        return new_matrix
    
    def rotate_matrix_by_pythonic(self, matrix: list) -> list:
        return [list(reversed(column)) for column in zip(*matrix)]
