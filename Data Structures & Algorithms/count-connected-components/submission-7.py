class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS with adjacency list to traverse all connected componenets.
        adj = { i: [] for i in range(n) }
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        res = 0
        
        # Visit all connected nodes starting from curr.
        def dfs(curr: int, prev: int):
            # Base case
            if curr in visited:
                return
            
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                dfs(nei, curr)
        
        for i in range(n):
            if i in visited:
                continue
            dfs(i, -1)
            res += 1
        
        return res

        
