# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS in pre-order

        # Return the number of good node at and before the node's level.
        def dfs(node, maxVal) -> int:
            # Base case
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0

            # Recursive
            res += dfs(node.left, max(node.val, maxVal))
            res += dfs(node.right, max(node.val, maxVal))
            return res
        
        return dfs(root, root.val)