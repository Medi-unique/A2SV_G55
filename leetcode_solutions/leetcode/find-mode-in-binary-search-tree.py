# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        count=defaultdict(int)

        def helper(node):
            
            if node:
                count[node.val]+=1
                if node.left:
                    helper(node.left)
                if node.right:
                    helper(node.right)
        helper(root)
        
        check=max(count.values())
        result=[]
        for key,val in count.items():
            if val == check:
                result.append(key)

        return result
        