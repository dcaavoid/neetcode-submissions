# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Core: find there is the split node
        # Method 1: iteration
        curr = root

        while curr:
            # Search left subtree when p and q are less than current node
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Search right subtree when p and q are greater than current node
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Split occurs and return
            else:
                return curr