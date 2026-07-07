# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS with in order traversal.
        # 1. Recursive
        # if not root:
        #     return None

        

        # 2. Iterative
        stack = []
        count = 0
        curr = root

        while curr or stack:
            # Push all left nodes into stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1
            
            if count == k:
                return curr.val
            
            curr = curr.right