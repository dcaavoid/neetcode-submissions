class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Backtrack b/c I need to try every possible position and then undo previous attempt before next.
        # There are four directions:
        # Horizontal, vertical, bottom-left to top-right, and top-left to bottom-right.
        # Top-left to bottom-right: row - col == constant
        # Bottom-left to top-right: row + col == constant
        res = []
        vertical = set()
        top_diag = set()    # row - col
        bot_diag = set()    # row + col
        board = [ ["." for _ in range(n)] for _ in range(n) ]

        # Given the row - 1 have valid queens, can I place a queen on row?
        def backtrack(row: int):
            # Base case
            if row == n:
                res.append(["".join(b) for b in board])    # How to join 2d matrix into 1d with comma-separated?
                return
            
            # Recursive: try each column in the current row.
            for col in range(n):
                # First check if there is any conflict
                if col in vertical or row - col in top_diag or row + col in bot_diag:
                    continue
                
                # Mark as visited and try
                vertical.add(col)
                top_diag.add(row - col)
                bot_diag.add(row + col)
                board[row][col] = "Q"
                backtrack(row + 1)

                # Undo previous attempt for next iteration
                vertical.remove(col)
                top_diag.remove(row - col)
                bot_diag.remove(row + col)
                board[row][col] = "."
        
        backtrack(0)
        return res
        

            