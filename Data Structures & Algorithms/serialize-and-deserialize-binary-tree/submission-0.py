# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Two versions in pre-order traversal with storing None (curr -> left -> right)
# 1. BFS
# class Codec:
    
#     # Encodes a tree to a single string.
#     def serialize(self, root: Optional[TreeNode]) -> str:

        
#     # Decodes your encoded data to tree.
#     def deserialize(self, data: str) -> Optional[TreeNode]:

# -------------------------------------------------------------------------------------
# 2. DFS
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Use an array to store the value at each node for easier reference in a recursive function.
        res = []

        # Append node's value/None into the serialized array.
        def dfs(node):
            # Base case
            if not node:
                res.append("None")
                return
            
            # Recursive
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0  # Use a global pointer to track which node is currently visiting.

        # Convert the serialized array back to nodes in the binary tree.
        def dfs():
            # Base case
            if values[self.i] == "None":
                self.i += 1     # Visit next node
                return None
            
            # Recursive
            node = TreeNode(int(values[self.i]))
            self.i += 1

            # Recursively visiting next node, don't need to update pointer i b/c it's in the recursive function.
            node.left = dfs()   
            node.right = dfs()

            return node
        
        return dfs()

