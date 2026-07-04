class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Did not even recognize that it's a linked list problem.
        # Did not recognize to use Floyd's Cycle Detection for this linked list problem.
        # Did not read the constraints carefully that 1 <= nums[i] <= n.
        # In Linked List: node.val=i, node.next=nums[i] b/c 1 <= nums[i] <= n.
        # Each pointer points to its index in the array.
        # Given the index is [0, n] and the range of numbers is [1, n],
        # starting at index 0, it will jump into the range [1,n] without jumping back to node 0.
        # If there are duplicate numbers, multiple pointers point to the same number of position in the array, creating a cycle.
        slow, fast = 0, 0

        # First iteration of Floyd's: find intersection of slow and fast
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Second iteration of Floyd's: find the start of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break
        
        return slow