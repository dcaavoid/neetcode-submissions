# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initial thought: DFS with searching the right first, and then left.
        # But don't understand how to track the height and return the right most at current height.
        # Three versions:
        # 1. BFS with right first, then left.
        # Time: O(N), space: O(N)
        # if not root:
        #     return []
        
        # queue = collections.deque([root])
        # res = []
        # height = 0

        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()

        #         # Add one node at right most per level
        #         if height == len(res):
        #             res.append(node.val)
                
        #         if node.right:
        #             queue.append(node.right)
                
        #         if node.left:
        #             queue.append(node.left)
            
        #     height += 1
        
        # return res

        # -----------------------------------------------------------------------------------------------
        # 2. BFS with left first then right to record the last node at each level.
        # if not root:
        #     return []
        
        # queue = collections.deque([root])
        # res = []

        # while queue:
        #     rightNode = None
        #     for _ in range(len(queue)):
        #         node = queue.popleft()

        #         if node:
        #             rightNode = node
        #             queue.append(node.left)
        #             queue.append(node.right)
            
        #     if rightNode:
        #         res.append(rightNode.val)
        
        # return res


        # -----------------------------------------------------------------------------------------------
        # 3. DFS with depth
        self.res = []

        def dfs(node, depth):
            # Base case
            if not node:
                return
            
            if depth == len(self.res):
                self.res.append(node.val)
            
            # Recursive: start from right
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return self.res

        

