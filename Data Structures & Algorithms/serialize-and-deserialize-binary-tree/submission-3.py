# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS in pre-order traversal
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        # Save node's value into res.
        def dfs(node):
            # Base case: save None string for deserialization.
            if not node:
                res.append("None")
                return
            
            # Recursive
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        # Turn array of results into a comma-seperated string.
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Turn the comma-seperated string into an array.
        values = data.split(",")
        # Pointer to track which value is currently visiting.
        self.i = 0

        # Return root by recursion.
        def dfs():
            # Base case
            if values[self.i] == "None":
                self.i += 1
                return

            # Recursive
            node = TreeNode(int(values[self.i]))
            self.i += 1
            # Since pre-order (curr -> left ->right), run recursion from left to right.
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


