# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def helper(node):
            nonlocal res
            
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            res = max(res, left + right)
            
            return max(left, right) + 1
        
        res = 0
        
        helper(root)
        
        return res
