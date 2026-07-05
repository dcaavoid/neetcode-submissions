# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Helper function 
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode
        head = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        head.next = l1 if l1 else l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Three versions:
        # 1. Divide and conquer in iteration: merge every two lists at a time, and perform log(k) times.
        # With mergeTwoLists helper function.
        # Time: O(N * log(k)), space: O(k) b/c the array stores max of k/2 head of linked lists in each iteration.
        
        # if not lists:
        #     return None
        
        # while len(lists) > 1:
        #     # Store the new head of merged linked lists.
        #     # Max length = k/2 in first iteration.
        #     mergedLists = []

        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i + 1] if i + 1 < len(lists) else None     # If odd number of linked lists remain
        #         mergedLists.append(self.mergeTwoLists(l1, l2))
            
        #     lists = mergedLists
        
        # return lists[0]

        # ------------------------------------------------------------------------
        # 2. Divide and conquer in recursion:
        # With mergeTwoLists and divide helper functions.
        # Time: O(N * log(k)), space: O(log(k)) b/c the depth of recursion is log(k), each recursion takes O(1) space.
        if not lists:
            return None
        
        return self.divide(lists, 0, len(lists) - 1)
    

    def divide(self, lists, left, right):
        # Base case:
        if left == right:
            return lists[left]
        
        # Recursive: divide and merge
        mid = (left + right) // 2
        l1 = self.divide(lists, left, mid)
        l2 = self.divide(lists, mid + 1, right)

        return self.mergeTwoLists(l1, l2)
        
        
        # ------------------------------------------------------------------------
        # 3. Heap

