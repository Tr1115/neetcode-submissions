# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            # Base case: empty tree has height 0
            if not node:
                return 0
            
            # Get heights of left and right subtrees
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            
            # Return the height of this node
            return 1 + max(left_height, right_height)

        if not root:
            return 0
        ans = 0 
        s = [root]
        while len(s):
            curr = s.pop()
            if curr:
                ans = max(ans, getHeight(curr.left) + getHeight(curr.right))
                s.append(curr.left)
                s.append(curr.right)
        return ans

