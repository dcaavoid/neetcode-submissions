class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi-source BFS starting from trasure chests (similar to leetcode 994).
        visited = set()    # (r, c): visited coordinate in grid
        q = collections.deque()   # Start with treasure chests only, and then append unvisited land.
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dist = 0   # Track the level of BFS from closest treasure chest.

        # Find out all treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        # Start BFS from treasure chests
        while q:
            # Track the level of BFS
            dist += 1

            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and col in range(COLS) and
                        (row, col) not in visited and
                        grid[row][col] != -1):
                        visited.add((row, col))
                        q.append((row, col))
                        grid[row][col] = dist