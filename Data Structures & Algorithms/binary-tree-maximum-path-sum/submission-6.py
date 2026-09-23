# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS
        # Create a global variable to track the max sum
        # max sum = curr + left + right
        # Pass the current subtree's max sum a a param in recursion
        # Curr sum = curr + max(left, right, 0)

        # Resolve the case when all nodes have negative values.
        self.res = root.val

        def dfs(node):
            # Base case
            if not node:
                return 0
            
            # Ignore negative subtrees
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Two choices at each node:
            # 1. If allow to split:
            self.res = max(self.res, node.val + left + right)
            # 2. Take only one subtree
            return node.val + max(left, right)
        
        dfs(root)
        return self.res