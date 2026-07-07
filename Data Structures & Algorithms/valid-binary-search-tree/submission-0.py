# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS with valid range
        # Start with (-inf, inf) to compare if the root node satisfies.
        # And for left subtree, update boundary to (-inf, node.val);
        # for right subtree, update boundary to (node.val, inf).

        def dfs(node, left, right):
            # Base case
            if not node:
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            # Recursive
            return (dfs(node.left, left, node.val) and
                    dfs(node.right, node.val, right))
        
        return dfs(root, float('-inf'), float('inf'))


