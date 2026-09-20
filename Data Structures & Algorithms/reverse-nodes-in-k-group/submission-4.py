# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy   # Last node from previous group

        while True:
            # 1. Find kth node
            kth = self.findKth(groupPrev, k)

            # Stop if there is less than k nodes in remaining list
            if not kth:
                break
            
            # 2. Reverse in group
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev. next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 3. Adjust pointers outside of current group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next
    

    def findKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
