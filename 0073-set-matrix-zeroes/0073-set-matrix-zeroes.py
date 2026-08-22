class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        first_col_zero = False

        # Use first row and first column to mark zeros
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Use the markers to set zeros
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0