class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS starting at each node
        ROWS, COLS = len(matrix), len(matrix[0])
        LIP = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # Length of the longest strictly increasing path starting (i, j).
        def dfs(i, j, prev):
            # Base case
            if (i < 0 or i == ROWS or j < 0 or j == COLS or
                matrix[i][j] <= prev):
                return 0
            
            if LIP[i][j] != 0:
                return LIP[i][j]
            
            # Recursive
            best = 1
            for dr, dc in directions:
                r, c = i + dr, j + dc
                candidate = 1 + dfs(r, c, matrix[i][j])
                best = max(best, candidate)

            LIP[i][j] = best
            return best
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP[r][c] = dfs(r, c, -1)
                res = max(res, LIP[r][c])
        
        return res