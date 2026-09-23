# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre-order: 1 2 3 4
        # in-order:  2 1 3 4
        self.pre_idx = 0    # Index of root node in preorder
        inorder_idx = { val: i for i, val in enumerate(inorder) }
        
        # [left, right]: inclusive range of inorder for current tree
        def dfs(left, right):
            # Base case
            if left > right:
                return None
            
            # Build current node and update number of visited roots
            val = preorder[self.pre_idx]
            root = TreeNode(val)
            self.pre_idx += 1

            # Find index of current node in inorder and split
            mid = inorder_idx[val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        
        return dfs(0, len(inorder) - 1)