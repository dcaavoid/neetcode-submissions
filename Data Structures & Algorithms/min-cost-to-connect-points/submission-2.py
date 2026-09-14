class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Find minimal spanning tree -> Prim's algo
        N = len(points)

        # Build adjacency list with all the cost of edges
        adj = { i: [] for i in range(N)} # i: list of [dist, point_j]
        for i in range(N):
            xi, yi = points[i]
            for j in range(i + 1, N):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's algo
        res = 0
        visited = set() # Track visited nodes
        minHeap = [[0, 0]]  # [dist, point] that are reachable

        while len(visited) < N:
            dist, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            
            res += dist
            visited.add(point)
            for neiDist, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiDist, nei])
        
        return res

