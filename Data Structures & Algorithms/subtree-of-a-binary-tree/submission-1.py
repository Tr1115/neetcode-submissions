# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def preOrder(self, root):
        if not root:
            return "$"
        return str(root.val) + self.preOrder(root.left) + self.preOrder(root.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        substring = self.preOrder(subRoot)
        string = self.preOrder(root)

        return substring in string