class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Adjacency list + DFS/BFS
        # Version 1: DFS on each node.
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set() # Why only need one?
        connected = 0

        def dfs(node, prev):
            # Base case
            if node in visited:
                return
            
            # Recursive
            visited.add(node)
            for node2 in adj[node]:
                if node2 == prev:
                    continue
                
                dfs(node2, node)
                visited.add(node2)
                

        for i in range(n):
            # If node i is already in a connected component.
            if i in visited:
                continue
            
            dfs(i, -1)
            connected += 1

        return connected


