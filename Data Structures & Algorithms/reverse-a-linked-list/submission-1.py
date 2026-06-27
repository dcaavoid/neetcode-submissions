# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Method 1: iteration: time: O(n), space: O(1)
        # prev, cur = None, head

        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        # return prev
        
        # Method 2: recursion: time: O(n), space: O(n)
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newHead
        
