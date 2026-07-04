# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First thought: two pointers
        # Slow starts at head, fast starts at nth node from the beginning, and both pointers move at the same speed;
        # Stop when fast.next=None, so slow stops one node front of the last nth node;
        # Create a dummy node when removing the first node
        dummy = ListNode(next=head)
        slow, fast = dummy, head

        # Move fast pointer to the nth node from the start of the linked list.
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers to find n-1th node from the end until fast is None.
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove nth from the end.
        slow.next = slow.next.next
        return dummy.next

