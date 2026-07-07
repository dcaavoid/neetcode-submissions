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
        # Two versions:
        # 1. BFS
        if not root:
            return []
        
        queue = deque([root])
        res = []
        height = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                # Add one node at right most per level
                if height == len(res):
                    res.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
            
            height += 1
        
        return res




        # -----------------------------------------------------------------------------------------------
        # 2. DFS