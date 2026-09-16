# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Don't know how many nodes
        # Two pointers that have constant distance of n + 1
        # Start from dummy node
        dummy = ListNode()
        dummy.next = head

        left, right = dummy, dummy
        for _ in range(n + 1):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        # Now left.next is the nth node from the end
        left.next = left.next.next

        return dummy.next

