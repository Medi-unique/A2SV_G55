# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # def helper(node):
        #     total=0
        #     if not node: return 0
        #     if low <= node.val <= high:
        #         print(total)
        #         total = node.val

        #     lsum=helper(node.left)
        #     rsum=helper(node.right)
        #     total += lsum+rsum
        #     return total
            

          
        # val=helper(root)
        # return val
        
        def helper(node):
            if not node: return 0
            total=0
            if low <= node.val <= high:
                total= node.val
            ls=helper(node.left)
            lr=helper(node.right)
            total += ls+lr
            return total
        val = helper(root)
        return val

        # def helper(node):
        #     result=0
        #     if not node: return 0
        #     if low <= node.val <= high:
        #         result += node.val
        #     if node.val < low:
        #         right = helper(node.right)
        #     if node.val >  high:
        #         left  = helper(node.left)
        #     return result + left +right
        # total = helper(root)
        # return total


        
