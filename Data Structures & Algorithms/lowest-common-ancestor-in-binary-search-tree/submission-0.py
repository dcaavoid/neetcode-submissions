# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Binary search tree: eliminate at most half of the tree each time.
        # Time complexity: O(log(N)) if the tree is balanced, or O(N) in worst case where the BST is unbalanced.
        # Space: O(1) if in iteration, or O(log(N)) in recursion.
        # 1. Iteration:
        # curr = root

        # # because p and q are both exist in the BST.
        # while curr:
        #     # Search right BST
        #     if p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     # Search left BST
        #     elif p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     # If two nodes split here, or one node happens to be the current node,
        #     # the current node is the LCA.
        #     else:
        #         return curr
        
        # ---------------------------------------------------------------------------
        # 2. Recursion
        # Search left BST
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
