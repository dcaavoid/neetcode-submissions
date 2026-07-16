class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP: top-down
        # rob(i) = max(nums[i] + rob(i + 2), rob(i + 1))
        # [rob1, rob2, n, n+1, n+2, ...]
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

