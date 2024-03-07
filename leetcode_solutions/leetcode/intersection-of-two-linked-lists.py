# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1,s2=headA,headB
        while s1 != s2:
            s1=s1.next if s1 else headB
            s2=s2.next if s2 else headA
        return s1
        