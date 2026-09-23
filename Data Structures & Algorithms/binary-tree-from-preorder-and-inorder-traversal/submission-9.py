# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            
            val = preorder[pre_left]
            node = TreeNode(val)
            mid = inorder_idx[val]
            left_size = mid - in_left
            
            node.left = helper(pre_left + 1, pre_left + left_size, in_left, mid - 1)
            node.right = helper(pre_left + left_size + 1, pre_right, mid + 1, in_right)
            return node
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)