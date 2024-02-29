# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(l,r):

            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            le=helper(l.left,r.right)
            ri= helper(l.right,r.left)
            return le and ri
        return helper(root.left,root.right)
        


        