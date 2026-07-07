# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS in pre-order
        self.count = 0

        def dfs(node, maxVal):
            # Base case
            if not node:
                return

            if node.val >= maxVal:
                self.count += 1
            
            dfs(node.left, max(node.val, maxVal))
            dfs(node.right, max(node.val, maxVal))
        
        dfs(root, float('-inf'))
        return self.count