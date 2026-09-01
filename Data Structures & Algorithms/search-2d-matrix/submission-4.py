class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search: first find row, then find column
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        left, right = 0, COLS - 1
        while left <= right:
            col = (left + right) // 2
            if target < matrix[row][col]:
                right = col - 1
            elif target > matrix[row][col]:
                left = col + 1
            else:
                return True
        
        return False
        