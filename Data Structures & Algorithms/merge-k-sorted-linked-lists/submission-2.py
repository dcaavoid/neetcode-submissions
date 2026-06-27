# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists
        
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, lf, rt) -> ListNode:
        if lf == rt:
            return lists[lf]
        
        mid = lf + (rt - lf) // 2
        left = self.divide(lists, lf, mid)
        right = self.divide(lists, mid + 1, rt)
        return self.mergeTwoLists(left, right)
        
            
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        start = ListNode()
        cur = start

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if list1 else list2
        return start.next