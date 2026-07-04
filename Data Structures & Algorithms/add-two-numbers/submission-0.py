# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # The original linked list follow the order of calculation;
        # Return the res pointer in reverse order.
        # Use a variable to track if one unit is proceed to the next.
        ones = False
        dummy = ListNode(None)
        curr = dummy
        p1, p2 = l1, l2

        # Create the linked list that represent sum in reverse order.
        while p1 and p2:
            value = p1.val + p2.val + 1 if ones else p1.val + p2.val
            ones = False

            if value // 10:
                ones = True
            
            curr.next = ListNode(val=value % 10)
            curr = curr.next
            p1, p2 = p1.next, p2.next
        
        # If any remaining nodes in either l1 or l2.
        while p1:
            value = p1.val + 1 if ones else p1.val
            ones = False

            if value // 10:
                ones = True
            
            curr.next = ListNode(val=value % 10)
            curr = curr.next
            p1 = p1.next
        
        while p2:
            value = p2.val + 1 if ones else p2.val
            ones = False

            if value // 10:
                ones = True
            
            curr.next = ListNode(val=value % 10)
            curr = curr.next
            p2 = p2.next

        # If there is one
        if ones:
            curr.next = ListNode(val=1)
            ones = False
        
        return dummy.next