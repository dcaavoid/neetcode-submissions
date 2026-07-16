class Solution:
    def rob(self, nums: List[int]) -> int:
        # Run DP twice
        # One edge case: if ther is only one number in the list.
        return max(nums[0], self.dp(nums[:-1]), self.dp(nums[1:]))

    def dp(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2