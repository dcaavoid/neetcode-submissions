class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Version 1: Adjacency list + DFS/BFS
        # adj = { i: [] for i in range(n) }
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)
        
        # visited = set() # Why only need one?
        # connected = 0

        # def dfs(node, prev):
        #     # Base case
        #     if node in visited:
        #         return
            
        #     # Recursive
        #     visited.add(node)
        #     for node2 in adj[node]:
        #         if node2 == prev:
        #             continue
                
        #         dfs(node2, node)

        # for i in range(n):
        #     # If node i is already in a connected component.
        #     if i in visited:
        #         continue
            
        #     dfs(i, -1)
        #     connected += 1

        # return connected

        # ----------------------------------------------------------------------------
        # Version 2: Union Find
        # Start with every node's root is itself.
        # For each connected pair of node, merge the small graph into larger graph's root.
        # Once a merge succeed, decrement total number of nodes by 1.
        res = n
        rank = [1] * n
        parents = [i for i in range(n)]

        # Return the root of node.
        def find(node):
            root = node

            while root != parents[root]:
                parents[root] = parents[parents[root]]  # Path compression
                root = parents[root]

            return root
        
        # Merge smaller graph to the root of the larger graph.
        # Return 1 if merge two graphs successfully, else return 0.
        def union(n1, n2) -> int:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            # If two graphs have different roots, merge smaller into larger one.
            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            
            return 1

        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
            