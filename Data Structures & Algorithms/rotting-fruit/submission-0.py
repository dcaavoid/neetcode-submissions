class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Traverse all the grids to add rotting oranges to the queue first.
        # Perform BFS with multiple sources.
        q = collections.deque()
        visited = set()   # (r, c): visited grid
        fresh = 0    # Count the number of fresh oranges remaining
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Find all rotten oranges.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                                
                if grid[r][c] == 1:
                    fresh += 1
        
        # Start rotting other fresh oranges if there is any fresh oranges remain.
        while q and fresh > 0:
            # Use len(q) to get a snapshot of current rotten oranges.
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Check valid fresh oranges.
                    if (row in range(ROWS) and col in range(COLS) and
                        (row, col) not in visited and grid[row][col] == 1):
                        fresh -= 1
                        visited.add((row, col))
                        q.append((row, col))
            
            time += 1
        
        return -1 if fresh else time