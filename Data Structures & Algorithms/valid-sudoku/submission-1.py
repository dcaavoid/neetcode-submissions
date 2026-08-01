class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Three sets: row, col, and 3*3 grid
        # For O(1) time check, use row/col/grid as key, hash set as value.
        # row = (row, -1); col = (col, -1); grid = (row // 3, col // 3)
        # Time: O(n^2), space: O(n^2)
        rows = {}    # row: set()
        cols = {}    # col: set()
        boxes = {}   # (row // 3, col // 3): set()
        n = len(board)

        for r in range(n):
            for c in range(n):
                # Skip empty grid
                if board[r][c] == ".":
                    continue
                
                # Intialize keys
                if r not in rows:
                    rows[r] = set()
                
                if c not in cols:
                    cols[c] = set()
                
                if (r // 3, c // 3) not in boxes:
                    boxes[(r // 3, c // 3)] = set()
                
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True