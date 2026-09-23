# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre-order: 1 2 3 4
        # in-order: 2 1 3 4
        # Base case
        # if not preorder or not inorder:
        #     return None
        
        # # Find index of the root node in inorder
        # root = TreeNode(preorder[0])
        # # index = number of nodes in the left subtree
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        # return root
        inorder_index = {val: i for i, val in enumerate(inorder)}  # O(1) lookup instead of O(n) scan
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None
            
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)
            
            mid = inorder_index[val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)