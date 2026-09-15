# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Iterative (two pointers: prev, curr)
        # Time: O(N); space: O(1)
        # prev, curr = None, head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev

        # 2. Recursive
        # 1 -> None
        # None <- 1 <- 2
        # 1 -> 2 -> 3 -> None
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return newHead

