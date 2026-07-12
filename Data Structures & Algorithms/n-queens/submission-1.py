class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Since a queen moves in three directions:
        # col: track conflict columns
        # posDiag: track conflict bottom-left to top right diagnoal
        # negDiag: track conflict top-left to bottom right diagnoal
        col = set()
        posDiag = set()   # r + c is constant
        negDiag = set()   # r - c is constant
        res = []
        board = [["."] * n for _ in range(n)]   # n * n matrix

        # Search for valid queen at row r.
        def backtrack(r: int):
            # Base case: have searched all rows and place queens.
            if r == n:
                board_copy = ["".join(row) for row in board]
                res.append(board_copy)
                return
            
            # Recursive: try each column given current row
            for c in range(n):
                # Continue to search next column is current column is not valid.
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)

                # Withdraw current selection
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res


