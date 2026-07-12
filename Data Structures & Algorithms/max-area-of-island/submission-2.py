class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Similar to Leetcode 200, can search four directions with either BFS or DFS.
        maxArea = 0     # Max area so far
        visited = set()   # (r, c): visited coordinate in grid.
        ROWS, COLS = len(grid), len(grid[0])

        # Given an unvisited grid[r][c], find the area of all connecting lands.
        def bfs(r: int, c: int):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            currArea = 1

            # Use BFS to search four directions
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and col in range(COLS) and
                        (row, col) not in visited and grid[row][col] == 1):
                        visited.add((row, col))
                        q.append((row, col))
                        currArea += 1
            
            return currArea


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea