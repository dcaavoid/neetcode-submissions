# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Identify the the previous node of this group, last node in this group, and first node of the next group.
        # Then reverse the order within the group.
        # Lastly, points the previous node of this group to the last node in this group,
        # and update the previous node pointer.
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            # Reverse the order within the group first.
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Adjust the pointer in prev and next groups.
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
    
        return dummy.next


    # Get the kth node of in the current group.
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
        