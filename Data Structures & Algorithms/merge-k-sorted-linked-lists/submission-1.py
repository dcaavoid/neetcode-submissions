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
        else:
            while len(lists) > 1:
                mergedLists = []
                
                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    list2 = lists[i + 1] if (i + 1) < len(lists) else None
                    mergedLists.append(self.mergeTwoLists(list1, list2))
                lists = mergedLists
        return lists[0]
        
            
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