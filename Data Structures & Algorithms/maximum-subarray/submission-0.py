class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Two choices: 1. add current number into subarray; 2. skip current number and clear subarray.
        # If current sum < 0, start a new subarray
        # backtrack (pop?) or dfs?
        # It's Greedy: remove negative prefix sum.
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            # Remove negative prefix sum
            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum