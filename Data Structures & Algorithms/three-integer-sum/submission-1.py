class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array first, and then iterate through all non-positive number, and then perform 2sum.
        # Question: how to ignore duplicate triplets?
        # Answer: The same value should not be used for the same role a second time.
        # [-4, -1, -1, -1, 0, 1, 2]
        nums.sort()
        res = []

        for i in range(len(nums)):
            # In a sorted array, the first number must be <= 0 so that the triplet sum can be 0.
            if nums[i] > 0:
                break

            # For the first number, the same number can be only searched once
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr = nums[left] + nums[right] + nums[i]

                if curr == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Update left/right pointer only to ignore duplicate numbers
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1
    
        return res

