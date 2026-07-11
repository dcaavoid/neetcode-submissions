# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS in level order traversal
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = collections.deque([root])
        res = []

        while queue:
            node = queue.popleft()

            if not node:
                res.append("None")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        if values[0] == "None":
            return None
        
        root = TreeNode(int(values[0]))
        queue = collections.deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()

            if values[i] != "None":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if values[i] != "None":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root

                

