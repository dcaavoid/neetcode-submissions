# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Pre-order: cur -> left -> right
        # In-order: left -> cur -> right
        # First value in pre-order is the root.
        # In in-order, any values on the left the root is the left subtree.
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])    # First value in pre-order is the root.
        mid = inorder.index(preorder[0])    # Get the numbers of elements on the left subtree from in-order.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root