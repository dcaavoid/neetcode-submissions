class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 sum = 1 pivot number + 2 sum
        # Sort the array first and choose non-positive numbers as the pivot number.
        # Find 2 sum that 2sum == abs(pivot number)
        # [-1, -0, -0, 0, 1, 2, -4]
        #   i   l            r
        # No duplicate triplets:
        #   1. skip duplicate pivot number;
        #   2. skip duplicate left pointer number.
        # Time: O(nlogn), space: O(1)
        nums.sort()
        res = []
        i = 0
        n = len(nums)
        while i < n:
            # Stop when pivot number is positive
            if nums[i] > 0:
                break

            # Skip all duplicate pivot number
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            
            # Find all combinations given current pivot number
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
        
        return res


