# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Merge two lists at a time -> Time: O(n log(k))
        # Empty list case
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            # Merge two lists at a time
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(list1, list2))
            
            lists = mergedLists
        
        return lists[0]

    # Helper function: merge two lists
    def mergeLists(self, list1, list2) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        # Both lists are non-empty
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # One of the lists is empty
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next