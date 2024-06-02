# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = []
        def list_all(root):
            if root:
                list_all(root.left)
                l.append(root.val)
                list_all(root.right)
        list_all(root)
        
        result = new_node = TreeNode(l[0])
        
        for i in l[1:]:
            new_node.right = TreeNode(i)
            new_node = new_node.right
            
        return result
