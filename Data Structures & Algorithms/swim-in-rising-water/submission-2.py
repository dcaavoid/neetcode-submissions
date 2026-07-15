class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Transform the question into find a path that minimize the maximum height.
        # Save [max(current height, previous height), coordinates] into min heap.
        visited = set()   # (row, col): visited coordinates
        minHeap = [[grid[0][0], 0, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited.add((0, 0))

        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return height
            
            # Append height, coordiate pairs from four directions into minHeap
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row < 0 or row == ROWS or col < 0 or col == COLS or
                    (row, col) in visited):
                    continue
                visited.add((row, col))   # Why we add visited here?
                heapq.heappush(minHeap, [max(height, grid[row][col]), row, col])