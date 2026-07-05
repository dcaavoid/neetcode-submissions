# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Two versions of DFS:
        # 1. in post-order: first reach the bottom, and then pass the max depth recursively.
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # -----------------------------------------------------------------------------
        # 2. in pre-order: pass the current depth while searching in DFS.
        self.max_depth = 0

        def dfs(node, depth):
            if not node:
                return
            
            self.max_depth = max(self.max_depth, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return self.max_depth