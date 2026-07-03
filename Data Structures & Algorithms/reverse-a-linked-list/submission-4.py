# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # How to deal with emtpy linked list?
        # Feel that I need recursion to start from the bottom.
        # Two ways:
        # 1. Iterative (two pointers: prev and curr)
        # Time: O(N), space: O(1)
        # prev, curr = None, head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return prev

        # 2. Recursive
        # Time: O(N), space: O(N)
        # Base case: if head is null or head is the last valid element
        if not head or not head.next:
            return head
        
        # Recursive:
        newHead = head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
