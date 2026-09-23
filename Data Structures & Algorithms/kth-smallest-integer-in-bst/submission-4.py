# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS in order traversal
        # Problem: how to track the kth node along traversing?
        # Method 1: recursive
        # self.count = 0  # Trach number of visited nodes
        # self.res = None

        # def dfs(node):
        #     # Base case: stop if reaches null node, or has found kth node
        #     if not node or self.res is not None:
        #         return
            
        #     # Recursive: in order traversal
        #     dfs(node.left)

        #     self.count += 1
        #     if self.count == k:
        #         self.res = node.val
        #         return
            
        #     dfs(node.right)
        
        # dfs(root)
        # return self.res

        # ==============================================================================
        # Method 2: iterative with stack
        stack = []
        count = 0
        curr = root

        while curr or stack:
            # In order: left -> root -> right
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1

            if count == k:
                return curr.val
            
            curr = curr.right