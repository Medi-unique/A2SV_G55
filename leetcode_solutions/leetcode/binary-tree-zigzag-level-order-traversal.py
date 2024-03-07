# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        curr=[]
        
        q = deque()
        flag=True
        if root:
           q.append(root)


        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()

                if node:

                    curr.append(node.val)
                    if node.left:q.append(node.left)
                    if node.right:q.append(node.right)
            if flag:
               result.append(curr)
               flag=False
            else:
                curr.reverse()
                result.append(curr)
                flag=True
            
            curr=[]
        




      
        return result

       



            

        