# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return 

            if node.val==val:
                print(node)
                return node

            if node.val < val:
                return helper(node.right)

            if node.val > val:
                return helper(node.left)
            # return node
            
        return helper(root)
        
        