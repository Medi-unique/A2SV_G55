# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        self.diff=0

        def helper(root,minval,maxval):
            if not root :
                return
            self.diff=max(self.diff,max(abs(minval - root.val),abs(maxval - root.val)))
            minval=min(minval,root.val)
            maxval=max(maxval,root.val)
            helper(root.left,minval,maxval)
            helper(root.right,minval,maxval)
            
        helper(root,root.val,root.val)
        return self.diff