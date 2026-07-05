# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS with a global variable to track max diameter.
        # DFS to return the max height of the current sub-tree.
        self.diameter = 0

        # Return the max depth of the current sub-tree while finding potential max diameter.
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Max diameter doesn't have to start form the root node,
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter