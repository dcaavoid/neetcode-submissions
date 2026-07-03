# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle node with two pointers.
        slow, fast = head, head.next    # Make sure the number of nodes in left <= right
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list;
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge the first and second half of the linked lists.
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
