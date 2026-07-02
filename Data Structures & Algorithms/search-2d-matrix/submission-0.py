class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search, but not sure how to implement in 2d.
        ROWS, COLS = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[ROWS - 1][COLS - 1]:
            return False
        
        # Search for row first using binary search
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        # Check if we find the valid row
        if top > bottom:
            return False
        
        # Search for col using binary search
        left, right = 0, COLS - 1
        while left <= right:
            col = (left + right) // 2

            if target > matrix[row][col]:
                left = col + 1
            elif target < matrix[row][col]:
                right = col - 1
            else:
                break
        
        return True if left <= right else False
        
