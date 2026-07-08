# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First find the kth node.
        # Then find the last node of previous group, and first node of the next group.
        # Within the current group, need two pointers to reverse the order in the group.
        # After that, point the last node of the previous group to the kth node.
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.findKth(groupPrev, k)
            # Skip if there are less than k nodes in this group.
            if not kth:
                break
            
            groupNext = kth.next
            curr = groupPrev.next
            prev = groupNext
            
            # Reverse the order within the group.
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next

    # Return the kth node from starting form node.
    def findKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node