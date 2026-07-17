class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Shortest path
        # Dijkstra algorithm (BFS) + min heap
        visited = set()         # Visited node
        minHeap = [(0, k)]      # (total time from k to v, v)
        time = 0
        edges = {i: [] for i in range(1, n + 1)}   # node i: (vi, ti)
        for u, v, t in times:
            edges[u].append((v, t))
        
        while minHeap:
            t, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            time = max(time, t)     # don't understand max use.
            
            for nei, neiTime in edges[u]:
                if nei not in visited:
                    heapq.heappush(minHeap, (t + neiTime, nei))   # Not very sure about t + neiTime.
            
        return time if len(visited) == n else -1