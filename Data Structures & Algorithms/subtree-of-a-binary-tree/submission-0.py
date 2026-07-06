# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS: first find the matching root, and then check left and right subtrees from there.
        # If root nodes don't match, keep searching until reaching the bottom.
        # Base case: a empty tree can be the sub root of any trees. 
        if not subRoot:
            return True
        
        if not root:
            return False

        # Recursive
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    # Return true if two trees are the same.
    def sameTree(self, node1, node2):
        # Base case
        if not node1 and not node2:
            return True
        
        # Recursive
        if node1 and node2 and node1.val == node2.val:
            return (self.sameTree(node1.left, node2.left) and
                    self.sameTree(node1.right, node2.right))

        return False            