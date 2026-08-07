class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimal spanning tree (Prim's algo)
        # Choose a minimal path between current MST and any unconnected points.
        n = len(points)
        
        # Build adjacency list of retrieving cost for each point
        adj = { i: [] for i in range(n)}    # point: lists of [cost, point] of its neighbor.
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        
        # Prim's algo
        visited = set()
        res = 0
        minHeap = [[0, 0]]
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)

            # Skip any visited points
            if i in visited:
                continue
            res += cost
            visited.add(i)

            # Iterate through point i's unconnected points
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))
        
        return res
            

