# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size,curr=0,head
        while curr:
            curr=curr.next
            size +=1
        
        curr=head
        need,add=size//k,size%k
        res=[]
        for i in range(k):
            res.append(curr)
            for j in range(need -1 +(1 if add else 0)):
                if not curr: break
                curr=curr.next
            if add > 0:
               add -=1 
            else:
                add-=0
            if curr:
                curr.next,curr=None,curr.next
        return res
            
        