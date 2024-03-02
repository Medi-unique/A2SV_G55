# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # left,right=ListNode(),ListNode()
        # lcurr=left
        # rcurr=right

        # while head:
        #     if head.val < x:
        #         lcurr.next=head
        #         lcurr=lcurr.next
        #     else:
        #         rcurr.next=head
        #         rcurr=rcurr.next
        #     head=head.next
        # # head=left.next
        # lcurr.next=rcurr.next
        # rcurr.next=None
        # return left.next

        left,right = ListNode(),ListNode()
        lcurr,rcurr=left,right

        while head:
            if head.val < x:
                lcurr.next=head
                lcurr=lcurr.next
            else:
                rcurr.next=head
                rcurr=rcurr.next
            head = head.next
        lcurr.next=right.next
        rcurr.next=None
        return left.next



        