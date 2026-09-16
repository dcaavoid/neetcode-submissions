class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra's algo + priority queue (minHeap: (weight, node))
        # First create an adjacency list
        edges = { i: [] for i in range(1, n + 1)}  # node: list of (node, time)
        for u, v, t in times:
            edges[u].append((v, t))
        
        # Djikstra's + minHeap to search shortest path
        minHeap = [(0, k)]  # (time, node)
        visited = set()
        res = 0

        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            if u1 in visited:
                continue
            visited.add(u1)
            # Use max b/c signal could travel in parallel
            res = max(t1, res)

            # Use BFS to add all reachable nodes
            for u2, t2 in edges[u1]:
                if u2 not in visited:
                    # Track cumulated cost from k to u2
                    heapq.heappush(minHeap, (t1 + t2, u2))
        
        return res if len(visited) == n else -1
