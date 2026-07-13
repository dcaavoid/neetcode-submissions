class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # r >= ROWS and c >= COLS -> Atlantic
        # r < 0 and c < 0 -> Pacific
        # But how to check both directions?
        # Start from the border of Pacific and Atlantic, do BFS to find all island that can reach them seperately.
        # Then return the intersection of two sets.
        # Two versions:
        # 1. DFS
        pac, atl = set(), set()   # (r, c): island that can reach either pacific or atlantic
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            # Base case: stop for invalid islands.
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in visited or heights[r][c] < prevHeight):
                return
            
            # Recursive
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        # Search from first row (Pacific) and last row (Atlantic)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])                 # First row for Pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])   # Last row for Atlantic
        
        # Search from the first column (Pacific) and last column (Atlantic)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        # Find intersections of two sets.
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

        # ------------------------------------------------------------------------------------------
        # 2. BFS