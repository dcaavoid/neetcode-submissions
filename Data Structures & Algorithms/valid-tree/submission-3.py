class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree: every node is connected, and there is no cycle.
        # Quick check: for n nodes, a valid tree has exactly n - 1 edges.
        # Question: since it's undirected edge, can I use topological sort?
        # In dfs, use a variable called prev to track the prev node.
        # --------------------------------------------------------------------------------
        # Version 1. DFS with adj
        # 0: [1, 2, 3]
        # 1: [0, 4]
        # 2: [0]
        # 3: [0]
        # 4: [1]
        # if len(edges) != n - 1:
        #     return False
        
        # adj = { i: [] for i in range(n) }
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)
        
        # visited = set()

        # # Given the previous node, can we create a valid tree from node?
        # def dfs(node: int, prev: int) -> bool:
        #     # Base case
        #     if node in visited:
        #         return False
            
        #     visited.add(node)
        #     for nei in adj[node]:
        #         # Since undirected edge (two ways)
        #         if nei == prev:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True
        
        # dfs(0, -1)
        # return len(visited) == n


        # ------------------------------------------------------------------------
        # Version 2: BFS
        if len(edges) != n - 1:
            return False
        
        adj = { i: [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        q = collections.deque()
        visited = set()
        q.append([0, -1])
        visited.add(0)

        while q:
            node, prev = q.popleft()
            for nei in adj[node]:
                if nei == prev:
                    continue
                if nei in visited:
                    return False
                
                visited.add(nei)
                q.append([nei, node])
        
        return len(visited) == n