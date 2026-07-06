# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if not root:
            return []

        queue = deque([root])
        res = []

        # Use a outer loop to control the level
        while queue:
            # Use a inner loop to iterate through all nodes at the current level.
            levelRes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levelRes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.append(levelRes)

        return res
        