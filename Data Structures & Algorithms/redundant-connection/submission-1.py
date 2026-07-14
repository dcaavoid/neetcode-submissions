class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Use Union Find to return the first edge that its two nodes have the same root.
        # By graph theory, a valid graph with n nodes only has n-1 edges, so there must be only one edge.
        # Nodes are [1, n] given there are n edges.
        n = len(edges)
        parents = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        # Return the root node of input node.
        def find(node):
            root = node

            while root != parents[root]:
                # Path compression for faster root retrival.
                parents[root] = parents[parents[root]]
                root = parents[root]
            
            return root
        
        # Merge two roots together by ranking.
        def union(node1, node2):
            if rank[node1] < rank[node2]:
                parents[node1] = node2
                rank[node2] += rank[node1]
            else:
                parents[node2] = node1
                rank[node1] += rank[node2]

        for n1, n2 in edges:
            p1, p2 = find(n1), find(n2)
            # Two nodes have the same root -> cycle
            if p1 == p2:
                return [n1, n2]
            else:
                union(p1, p2)