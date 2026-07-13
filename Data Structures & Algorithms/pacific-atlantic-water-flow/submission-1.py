class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # r >= ROWS and c >= COLS -> Atlantic
        # r < 0 and c < 0 -> Pacific
        # But how to check both directions?
        # Start from the border of Pacific and Atlantic, do BFS to find all island that can reach them seperately.
        # Then return the intersection of two sets.
        # Two versions:
        # 1. DFS
        # pac, atl = set(), set()   # (r, c): island that can reach either pacific or atlantic
        # ROWS, COLS = len(heights), len(heights[0])

        # def dfs(r, c, visited, prevHeight):
        #     # Base case: stop for invalid islands.
        #     if (r < 0 or r == ROWS or c < 0 or c == COLS or
        #         (r, c) in visited or heights[r][c] < prevHeight):
        #         return
            
        #     # Recursive
        #     visited.add((r, c))
        #     dfs(r - 1, c, visited, heights[r][c])
        #     dfs(r + 1, c, visited, heights[r][c])
        #     dfs(r, c - 1, visited, heights[r][c])
        #     dfs(r, c + 1, visited, heights[r][c])

        # # Search from first row (Pacific) and last row (Atlantic)
        # for c in range(COLS):
        #     dfs(0, c, pac, heights[0][c])                 # First row for Pacific
        #     dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])   # Last row for Atlantic
        
        # # Search from the first column (Pacific) and last column (Atlantic)
        # for r in range(ROWS):
        #     dfs(r, 0, pac, heights[r][0])
        #     dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        # # Find intersections of two sets.
        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])
        
        # return res

        # ------------------------------------------------------------------------------------------
        # 2. BFS
        pac, atl = set(), set()     # (r, c): visited island that can flow into Pacific/Atlantic.
        ROWS, COLS = len(heights), len(heights[0])
        pac_q, atl_q = collections.deque(), collections.deque()  # Queue for border islands of Pacific/Atlantic
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Append border islands into queue for BFS
        for c in range(COLS):
            pac_q.append((0, c))
            pac.add((0, c))
            atl_q.append((ROWS - 1, c))
            atl.add((ROWS - 1, c))
        
        for r in range(ROWS):
            pac_q.append((r, 0))
            pac.add((r, 0))
            atl_q.append((r, COLS - 1))
            atl.add((r, COLS - 1))

        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # Valid, unvisited island.
                    if (row in range(ROWS) and col in range(COLS) and
                        (row, col) not in visited and
                        heights[row][col] >= heights[r][c]):
                        visited.add((row, col))
                        q.append((row, col))
        
        # Start BFS
        bfs(pac_q, pac)
        bfs(atl_q, atl)

        # Find intersection of two sets.
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
        