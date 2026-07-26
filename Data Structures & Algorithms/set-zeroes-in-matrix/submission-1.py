class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # first row = True
        # 1 2 3 4 0
        # 8 6 8 6 0
        # 7 2 9 6 1
        # m = 5, n = 3
        # Modify in-place b/c we traverse from left to right, top to bottom.
        # matrix[0][0:n-1] = 0: this column is 0
        # matrix[1:m-1][0] = 0: this row (except first row) is 0
        first_row = False
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row = True
                    else:
                        matrix[row][0] = 0
                    matrix[0][col] = 0
                    
        
        # First set rows 1:m-1 to 0
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0

        # Then set columns 0:n-1 to 0
        for col in range(n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0

        # Lastly set first row to 0 if first_row is True
        if first_row:
            for col in range(n):
                matrix[0][col] = 0