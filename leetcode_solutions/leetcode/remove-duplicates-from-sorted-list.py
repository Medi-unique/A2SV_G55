# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        if not curr:
            return 
        
        while curr.next:
            check=curr.next
            if check.val == curr.val:
               curr.next=check.next
            else:
            
                curr= curr.next
        return head

        