"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Version 1: DFS
        # if not node:
        #     return None
        
        # oldToNew = {}   # original node -> copy of node

        # # Return the copy of the node with its copied neighbors.
        # def dfs(node):
        #     # Base case: the copy exists
        #     if node in oldToNew:
        #         return oldToNew[node]
            
        #     # Create a copy when it doesn't exist
        #     copy = Node(node.val)
        #     oldToNew[node] = copy

        #     # Build neighbors for copy node
        #     for n in node.neighbors:
        #         copy.neighbors.append(dfs(n))
            
        #     return copy
        
        # return dfs(node)

        # Version 2: BFS
        if not node:
            return None
        
        oldToNew = { node: Node(node.val)}   # key=original node, value=copy of new node
        q = collections.deque([node])

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    q.append(n)
                
                oldToNew[curr].neighbors.append(oldToNew[n])
        
        return oldToNew[node]
        