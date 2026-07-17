class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # curMax: local max product of subarray ending at nums[i]
        # curMin: local min product of subarray ending at nums[i]
        # 0 check is unnecessary b/c we set curMax and curMin to nums[i] in the next itartion after meeting 0.
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            temp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        
        return res
