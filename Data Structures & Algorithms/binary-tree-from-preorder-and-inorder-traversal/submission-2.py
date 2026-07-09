# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Pre-order: curr -> left -> right
        # In-order: left -> curr -> right
        # DFS in recursion: use first node in pre-order as the root, find the index of root in in-order,
        # Build left subtree, and then recursively to go the right.
        # Base case
        if not preorder or not inorder:
            return None
        
        # Recursive
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return root