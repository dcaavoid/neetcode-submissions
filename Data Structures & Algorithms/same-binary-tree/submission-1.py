# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # From top down, but how to early exit once one of the node doesn't match?
        # Base case
        if not p and not q:
            return True
        # equivalent to (not p and q) or (not q and p) with not p and not q in front
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))