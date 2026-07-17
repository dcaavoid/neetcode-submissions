class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree = no cycle + all nodes are connected.
        # Version 1: Use Adj list + DFS to search for cycle
        # Errors in initial attempts: Ignored edge cases in undirected edges and disconnected nodes.
        # Question: since undirected, each edge is in two directions, how to use set to save cycle and safe nodes?
        # adj = { i: [] for i in range(n) }
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)

        # visited = set()

        # # Return False if there is cycle in visited nodes.
        # def dfs(node, prev) -> bool:
        #     # Base case
        #     if node in visited:
        #         return False
            
        #     # Recursively check all connecting nodes (but not previous node)
        #     visited.add(node)
        #     for node2 in adj[node]:
        #         # SInce undirected edge goes both ways, skip previous node.
        #         if node2 == prev:
        #             continue
        #         if not dfs(node2, node):
        #             return False
            
        #     return True
        
        # prev = -1 b/c -1 is not a valid node.
        # dfs(0, -1)
        # return len(visited) == n

        # -------------------------------------------------------------------------------------
        # Version 2: BFS
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        q = collections.deque([(0, -1)])    # (node, prev): save node and its previous node
        visited.add(0)

        while q:
            node, prev = q.popleft()
            for node2 in adj[node]:
                if node2 == prev:
                    continue
                if node2 in visited:
                    return False
                
                visited.add(node2)
                q.append((node2, node))
        
        return len(visited) == n