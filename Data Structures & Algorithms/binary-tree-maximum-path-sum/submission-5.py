# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS
        # For each root node, there are two choices:
        # 1. root node + two subtrees to make a path;
        # 2. root node + max(left, right) to pass back to its root node.
        self.res = root.val
        
        # Return the path sum given node is the top node.
        # While update a global variable self.res to keep track the possible max sum when two subtrees are considered.
        def dfs(node):
            # Base case
            if not node:
                return 0
            
            # Recursive
            # Ignore negative sum path.
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.res = max(self.res, left + right + node.val)
            return node.val + max(left, right)
        
        dfs(root)
        return self.res