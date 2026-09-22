# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS to track the max value along the path
        def dfs(node, maxVal) -> int:
            # Base case
            if not node:
                return 0
            
            # Check if current node is a good node
            res = 1 if node.val >= maxVal else 0

            # Recursive
            res += dfs(node.left, max(node.val, maxVal))
            res += dfs(node.right, max(node.val, maxVal))
            return res
        
        return dfs(root, float("-inf"))