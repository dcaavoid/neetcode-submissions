# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion in DFS: either pre-order (swap the current nodes first) or post-order (run recursion first)
        # Base case:
        if not root:
            return None

        # Recursive in post-order
        # temp = root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(temp)
        

        # Recursive in pre-order
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
