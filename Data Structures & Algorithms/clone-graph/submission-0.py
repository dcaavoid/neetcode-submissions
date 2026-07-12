"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map + DFS/BFS
        # 1. DFS: recursively build a copy if the copy doesn't exist,
        #         and then search all its neighbors.
        if not node:
            return None
        
        oldToNew = {}   # old node: new node

        def dfs(node):
            # Base case: if the current node's copy exist, return its copy.
            if node in oldToNew:
                return oldToNew[node]
            
            # Recursive: if the current node's copy doesn't exist, create its copy and search its neighbor.
            newNode = Node(node.val)
            oldToNew[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))
            
            return newNode
        
        return dfs(node)