# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        # when we return the node we are also returning the values associated with it alse
        # if we were asked only the middle value we can return slow.val
        return slow

        