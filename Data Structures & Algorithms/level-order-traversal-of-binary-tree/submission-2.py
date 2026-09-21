# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Method 1: Level order = BFS with queue
        # Special case: empty tree
        # if not root:
        #     return []
        
        # queue = collections.deque([root])
        # res = []    # 2D List

        # while queue:
        #     level_res = []
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         level_res.append(node.val)
                
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        #     res.append(level_res)
        
        # return res

        # ------------------------------------------------------------------------
        # Method 2: recursion that add node.val to index=height in result list
        res = []    # 2D list

        def dfs(node, height):
            # Base case
            if not node:
                return
            
            # res has one new sub-list per depth level the first time that depth is reached
            if len(res) == height:
                res.append([])
            res[height].append(node.val)

            # Recursive
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
        
        dfs(root, 0)
        return res

