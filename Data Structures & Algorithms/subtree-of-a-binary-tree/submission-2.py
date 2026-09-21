# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Method 2: serialize into strings using pre-order -> Time: O(n + m)
        def serialize(node):
            if not node:
                return "#"
            
            return "^" + str(node.val) + serialize(node.left) + serialize(node.right)
        
        root_str = serialize(root)
        subRoot_str = serialize(subRoot)

        return subRoot_str in root_str

    #     # First steps: 1. check if root and subRoot are the same tree;
    #     #              2. if not, check if children of root is the same treee as subRoot
    #     # Base case:
    #     # 1. An empty tree is a subtree of any trees.
    #     if not subRoot:
    #         return True
    #     # 2. An empty root tree cannot hold any unempty trees.
    #     if not root:
    #         return False
    #     # 3. Check if they are same trees.
    #     if self.sameTree(root, subRoot):
    #         return True
        
    #     # Recursive: check childen trees of root
    #     return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    

    # # Helper function to check if two trees are the same.
    # def sameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
    #     # Base case
    #     # Empty trees are the same
    #     if not r1 and not r2:
    #         return True
    #     # If one of the trees is empty, or values of two unempty tree are different.
    #     if not r1 or not r2 or r1.val != r2.val:
    #         return False
        
    #     # Recursive
    #     return (self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right))