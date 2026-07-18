class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Version 1. Dynamic Programming
        # Time: O(N^2); space: O(N)
        # LIS = [1] * len(nums)

        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        
        # return max(LIS)

        # Version 2. Binary search (don't understand)
        # Time: O(N*log(N))
        tails = []

        for n in nums:
            left, right = 0, len(tails)
            
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= n:
                    right = mid
                else:
                    left = mid + 1
            
            if left == len(tails):
                tails.append(n)
            else:
                tails[left] = n
        
        return len(tails)