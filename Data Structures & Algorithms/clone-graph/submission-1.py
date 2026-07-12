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
        # if not node:
        #     return None
        
        # # Use a hash map to store copy of nodes without causing cycle or duplicate node error.
        # oldToNew = {}   # old node: new node

        # def dfs(node):
        #     # Base case: if the current node's copy exist, return its copy.
        #     if node in oldToNew:
        #         return oldToNew[node]
            
        #     # Recursive: if the current node's copy doesn't exist, create its copy and search its neighbor.
        #     # Should create a copy of the node first b/c neighbors may point back to the current node.
        #     newNode = Node(node.val)
        #     oldToNew[node] = newNode
        #     for n in node.neighbors:
        #         newNode.neighbors.append(dfs(n))
            
        #     return newNode
        
        # return dfs(node)


        # ------------------------------------------------------------------------------------------
        # 2. BFS with hash map
        # First append first node into the queue.
        # For each node's neighbor, if it doesn't have copy, create a copy, save to hash map, and append to queue for searching its neighbor in the future.
        if not node:
            return None
        
        oldToNew = {node: Node(node.val)}
        q = collections.deque([node])

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    q.append(n)
                
                oldToNew[curr].neighbors.append(oldToNew[n])
        
        return oldToNew[node]