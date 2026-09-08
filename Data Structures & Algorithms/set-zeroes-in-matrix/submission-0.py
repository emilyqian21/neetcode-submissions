class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # Time: O(m * n)
        # Space: O(1)
        #
        # Use the first row and first column as markers:
        # matrix[r][0] == 0 -> row r should be zero
        # matrix[0][c] == 0 -> col c should be zero

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check whether first row originally contains 0
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True

        # Check whether first column originally contains 0
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True

        # Use first row / first col to mark rows and cols
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero the inner matrix based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle first row
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Handle first column
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0