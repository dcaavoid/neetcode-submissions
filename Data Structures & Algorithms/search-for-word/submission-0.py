class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Simplier version of Leetcode 212: Word Search II.
        # Backtracking
        # Use a set to track the current visited coordiates.
        # Use a pointer i to track which character are we visiting at word.
        visited = set()   # (x, y): visited coords in board in curr backtrack.
        ROWS, COLS = len(board), len(board[0])

        def backtrack(x, y, i) -> bool:
            # Base case:
            # If word[0, i - 1] characters pass, we find the word.
            if i == len(word):
                return True

            # False cases: 
            # 1. If current coordinate is visited;
            # 2. If coordinate is out of bound in board;
            # 3. If current pointer's character doesn't match board[x][y].
            if (x < 0 or x == ROWS or
                y < 0 or y == COLS or
                (x, y) in visited or
                board[x][y] != word[i]):
                return False
            
            # Recursive
            visited.add((x, y))
            found = (backtrack(x + 1, y, i + 1) or
                     backtrack(x - 1, y, i + 1) or
                     backtrack(x, y + 1, i + 1) or
                     backtrack(x, y - 1, i + 1))

            visited.remove((x, y))
            return found
        
        # Try each grid as the starting grid.
        for x in range(ROWS):
            for y in range(COLS):
                if backtrack(x, y, 0):
                    return True
        
        return False