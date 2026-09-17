class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # turn the list into a linked list
        # val: index i at nums; next: value at nums[i]
        # Repeated integer = two values at different index point to the same index = start of the cycle
        # Start at nums[0] is safe b/c the range is [1, n] inclusive
        slow, fast = nums[0], nums[0]
        
        # Find
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Find start of the cycle
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow