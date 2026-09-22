# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # Instead of comparing every node to its subtree, which takes O(n^2) time,
        # Set a valid range (lower, upper) for each node
        def dfs(node, lower, upper):
            # Base case
            if not node:
                return True
            
            # Check if the current node is in the valide range
            if not (node.val > lower and node.val < upper):
                return False
            
            # Recursive
            return (dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper))
        
        return dfs(root, float("-inf"), float("inf"))