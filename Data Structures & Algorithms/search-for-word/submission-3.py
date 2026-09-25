class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        ROWS, COLS = len(board), len(board[0])
        visited = set()     # Visited coordinate in current dfs
        directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        
        # Start at (r, c) in board, is the word[i] in path?
        def dfs(r, c, i) -> bool:
            # Base case:
            # 1. all characters in word matches in board
            if i == len(word):
                return True

            # 2. if out of bound or visited or don't match the character
            if (r < 0 or r >= ROWS or
               c < 0 or c >= COLS or
               (r, c) in visited or 
               board[r][c] != word[i]):
               return False
            
            # Recursive
            visited.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if dfs(row, col, i + 1):
                    return True

            # Undo for future dfs visit
            visited.remove((r, c))
            return False
        
        # Try each coordinate as the start
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False