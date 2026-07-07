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
        self.count = 0
        self.res = None

        def dfs(node):
            # Base case
            if not node:
                return
            
            # Recursive
            # Left
            dfs(node.left)

            # Current node
            self.count += 1
            if self.count == k:
                self.res = node.val
            
            # Right
            dfs(node.right)
        
        dfs(root)
        return self.res
        

        # 2. Iterative
        # stack = []
        # count = 0
        # curr = root

        # while curr or stack:
        #     # Push all left nodes into stack
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()
        #     count += 1
            
        #     if count == k:
        #         return curr.val
            
        #     curr = curr.right