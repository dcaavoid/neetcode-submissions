class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linked list: node: index, pointer = nums[index]
        # If there is a cycle in the linked list, the start of the cycle is the repeated number.
        # Since there are n + 1 numbers ranging from [1, n], starting the node at index 0 will not create a cycle pointing back to index 0.
        slow, fast = 0, 0

        # Since we are guaranteed to find the repeated number.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow