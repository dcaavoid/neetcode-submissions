# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # DFS pre-order
        res = []

        def dfs(node):
            # Base case
            if not node:
                res.append("N")
                return
            
            # Recursive (pre-order)
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # DFS pre-order
        values = data.split(",")
        self.index = 0

        def dfs():
            # Base case
            if values[self.index] == "N":
                self.index += 1
                return None
            
            # Recursive (pre-order)
            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()



