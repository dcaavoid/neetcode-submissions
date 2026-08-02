class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Version 2: Union Find
        parent = [i for i in range(n)]  # index i = parent of node i
        rank = [1] * n    # index i = number of nodes in graph with parent node i
        
        # Return the root of node
        def find(node: int) -> int:
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        # Merge connected nodes, and return 1 if merge together or 0 if already merged.
        def union(n1: int, n2: int) -> int:
            p1, p2 = find(n1), find(n2)
            
            # Already merged
            if p1 == p2:
                return 0
            
            # Not merged yet
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        res = n
        for a, b in edges:
            res -= union(a, b)
        
        return res

        # ------------------------------------------------------------------------
        # Version 1: DFS with adjacency list to traverse all connected componenets.
        # adj = { i: [] for i in range(n) }
        # for a, b in edges:
        #     adj[a].append(b)
        #     adj[b].append(a)
        
        # visited = set()
        # res = 0
        
        # # Visit all connected nodes starting from curr.
        # def dfs(curr: int, prev: int):
        #     # Base case
        #     if curr in visited:
        #         return
            
        #     visited.add(curr)
        #     for nei in adj[curr]:
        #         if nei == prev:
        #             continue
        #         dfs(nei, curr)
        
        # for i in range(n):
        #     if i in visited:
        #         continue
        #     dfs(i, -1)
        #     res += 1
        
        # return res