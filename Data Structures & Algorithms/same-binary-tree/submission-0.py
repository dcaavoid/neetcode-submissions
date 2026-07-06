# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS in pre-order to check the current node first before doing down to next subtrees.
        # Base case
        # If both are null nodes, they are the same.
        # if not p and not q:
        #     return True
        # # If one of the nodes is not null, or the value at two nodes are different, they are different.
        # if not p or not q or p.val != q.val:
        #     return False

        # # Recursive
        # return (self.isSameTree(p.left, q.left) and
        #         self.isSameTree(p.right, q.right))        
        
        # --------------------------------------------------------------------------------------------
        # In BFS: iterate the queue that stores the nodes at current level, and compare each node.
        # Store (p, q) nodes pair.
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.pop()

            if not node1 and not node2:
                continue
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True
