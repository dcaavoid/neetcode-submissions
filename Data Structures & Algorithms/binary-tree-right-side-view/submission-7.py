# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Method 1: BFS that only returns the last node at each level
        # Empty case
        # if not root:
        #     return []
        # queue = collections.deque([root])
        # res = []
        # while queue:
        #     level = len(queue)
        #     for i in range(level):
        #         node = queue.popleft()
        #         # Add the last element at this level
        #         if i == level - 1:
        #             res.append(node.val)
        #         # Add not null children
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return res

        # ===========================================================================
        # Method 2: BFS with right first then last
        # if not root:
        #     return []
        
        # queue = collections.deque([root])
        # height = 0
        # res = []

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         # Add first node from right
        #         if height == len(res):
        #             res.append(node.val)
                
        #         # Add right then left
        #         if node.right:
        #             queue.append(node.right)
        #         if node.left:
        #             queue.append(node.left)
        #     height += 1
        # return res

        # ===========================================================================
        # Method 3: recursively check from right to left
        res = []

        # Recursive helper function
        def dfs(node, depth):
            # Base case
            if not node:
                return
            
            # Add first node from right
            if len(res) == depth:
                res.append(node.val)
            
            # Recusive
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res