# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Use DFS to search for the max gain from visiting node + left or right subtree.
        # Don't include negative left or right subtree in the return of recursion.
        # Use a gloabl variable to keep track the max gain without splitting from node.
        self.res = root.val

        # Return the max gain from splitting at node.
        def dfs(node) -> int:
            # Base case
            if not node:
                return 0
            
            # Recursive
            # Get rid of negative child subtree b/c it will make the sum smaller.
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Check if including both left and right subtress make the max path.
            self.res = max(self.res, node.val + left + right)

            # Return max gain by splitting at node.
            return max(left, right) + node.val
        
        dfs(root)
        return self.res
            