# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS that only returns the last node at each level
        # Empty case
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []

        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()

                # Add the last element at this level
                if i == level - 1:
                    res.append(node.val)
                
                # Add not null children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res