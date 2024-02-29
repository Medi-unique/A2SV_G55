# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]

        def helper(node):
            if node:
                helper(node.left)
                res.append(node.val)
                helper(node.right)
                return node

        helper(root)
        for i  in range(1,len(res)):
            if res[i-1]== res[i]:
                return False

        final= sorted(res)

        return res == final
        
        