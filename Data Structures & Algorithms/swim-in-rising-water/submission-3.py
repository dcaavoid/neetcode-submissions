class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Equivalent: find a path that max elevation is minimized
        # Build a minHeap to track the elevation (that gets this square) and coordinate
        # BFS to search adjacent squares
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = []    # (time, row, col)
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        visited = set()     # Visited coordinates: (row, col)
        visited.add((0, 0))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            # Return if reaches bottom right square
            if row == ROWS - 1 and col == COLS - 1:
                return time
            
            # Add neighboring squares to the minHeap
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                # Boundary check
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    continue

                # Skip visited squares or add unvisited squares
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                heapq.heappush(minHeap, (max(grid[r][c], time), r, c))