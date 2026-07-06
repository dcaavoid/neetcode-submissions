# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Don't know how to keep track the height while returning bool.
        # Ans: write a helper function that stores [bool, height]
        # Use DFS with post-order to eliminate redundency of calculation.

        # def dfs(node):
        #     # Base case
        #     if not node:
        #         return [True, 0]
            
        #     # Recursive
        #     left, right = dfs(node.left), dfs(node.right)
        #     balanced = (left[0] and
        #                 right[0] and
        #                 abs(left[1] - right[1]) <= 1)
        #     return [balanced, 1 + max(left[1], right[1])]
        
        # return dfs(root)[0]

        # Version 2: early stop by returning senital value -1 to represent unbalance.
        
        # Return height of subtrees in post-order
        # If unbalanced, just return -1.
        def dfs(node):
            # Base case
            if not node:
                return 0
            
            # Recursive
            left = dfs(node.left)
            if left == -1:
                return -1
            
            right = dfs(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return dfs(root) != -1