class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Three sets: row, col, and 3*3 grid
        # For O(1) time check, use row/col/grid as key, hash set as value.
        # row = (row, -1); col = (col, -1); grid = (row // 3, col // 3)
        # Time: O(n^2), space: O(n^2)
        sudoku = {}   # (row, col): set()
        n = len(board)

        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    continue

                if (row, -1) not in sudoku:
                    sudoku[(row, -1)] = set()
                
                if (-1, col) not in sudoku:
                    sudoku[(-1, col)] = set()
                
                if (row // 3, col // 3) not in sudoku:
                    sudoku[(row // 3, col // 3)] = set()
                    
                if (board[row][col] in sudoku[(row, -1)] or
                    board[row][col] in sudoku[(-1, col)] or
                    board[row][col] in sudoku[(row//3, col//3)]):
                    return False
                
                sudoku[(row, -1)].add(board[row][col])
                sudoku[(-1, col)].add(board[row][col])
                sudoku[(row // 3, col // 3)].add(board[row][col])
        
        return True