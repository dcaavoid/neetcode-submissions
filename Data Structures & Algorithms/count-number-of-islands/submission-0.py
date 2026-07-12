class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS but don't know to how to implement exactly.
        # Two versions:
        # 1. BFS
        rows, cols = len(grid), len(grid[0])
        visited = set()     # (r, c): visited in grid
        islands = 0

        # Put all connecting islands' coordinates into the visited set.
        def bfs(r: int, c: int): 
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))

        # Try every grid as a possible start of land.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)   # Search all connecting islands to (r, c)
                
        return islands
        


        # ------------------------------------------------------------------
        # 2. DFS