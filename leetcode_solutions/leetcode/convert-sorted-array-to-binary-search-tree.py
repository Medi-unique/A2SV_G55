# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l,r = 0,len(nums)
        def helper(l,r):
            if l > r:
                return None

            mid = (l+r)// 2
            print(mid)
            
            left=helper(l,mid-1)
            right=helper(mid+1,r)
            return TreeNode(nums[mid],left,right)
        return helper(l,r-1)
    
        