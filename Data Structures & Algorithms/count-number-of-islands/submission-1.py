class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS but don't know to how to implement exactly.
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()     # (r, c): visited in grid
        islands = 0

        # Two versions:
        # 1. BFS by connecting surrounding lands when we find an unvisited land.
        # Use queue for BFS b/c first-in-first-out.
        # Put all connecting islands' coordinates into the visited set.
        # def bfs(r: int, c: int): 
        #     q = collections.deque()
        #     visited.add((r, c))
        #     q.append((r, c))
        #     directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        #     while q:
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(ROWS) and
        #                 c in range(COLS) and
        #                 grid[r][c] == "1" and
        #                 (r, c) not in visited):
        #                 visited.add((r, c))
        #                 q.append((r, c))
        
        # ------------------------------------------------------------------
        # 2. DFS
        # Use stack for DFS b/c last-in-first-out.
        def dfs(r: int, c: int):
            # Base case
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] != "1" or
                (r, c) in visited):
                return
            
            # Recursive: valid, unvisited island
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        # Try every grid as a possible start of land.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    # Search all connecting islands to (r, c)
                    # bfs(r, c)
                    dfs(r, c)
                
        return islands
