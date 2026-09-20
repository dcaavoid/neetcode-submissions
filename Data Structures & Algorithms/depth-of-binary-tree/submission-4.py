# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 3 methods:
        # Method 1: recursive DFS -> Time O(n), space O(n)
        # if null: 0; else: 1 + max(dfs(left), right)
        # Base case
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # ----------------------------------------------------------------------------
        # Method 2: iterative DFS
        if not root:
            return 0
        
        stack = [[root, 1]] # [node, current depth]
        res = 0

        while stack:
            node, depth = stack.pop()
            res = max(depth, res)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        return res

        # ----------------------------------------------------------------------------
        # Method 3: BFS
        # if not root:
        #     return 0
        
        # queue = collections.deque([root])
        # depth = 0

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
                
        #     depth += 1
        
        # return depth
