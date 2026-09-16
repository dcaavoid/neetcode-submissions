# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Figure out how to carry number
        # Problem: two linked lists might be in different length
        carry = False
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry:
            # First add the carry 1 from the previous calculation
            if carry:
                digit = 1
                carry = False
            else:
                digit = 0
            
            # Add available digits
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
            
            # Deal with carry
            if digit // 10:
                carry = True
            digit %= 10
            curr.next = ListNode(digit)
            curr = curr.next
        
        return dummy.next
            
            