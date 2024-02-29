# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(l,r):
            if not l and not r:
                return
            if l and not r:
                return l
            if r and not l:
                return r
            if l and r:
                l.val += r.val
            l.right=helper(l.right,r.right)
            l.left=helper(l.left,r.left)
            return l
        return helper(root1,root2)