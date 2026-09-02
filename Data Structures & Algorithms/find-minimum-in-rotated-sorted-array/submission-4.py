class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. Binary search to compare with right (left is the min)
        left, right = 0, len(nums) - 1
        # Do not set left <= right b/c we want to converge left and right to a single index, which is the min value's index.
        while left < right:
            mid = (left + right) // 2
            # [mid, right] contains rotatation
            if nums[mid] > nums[right]:
                left = mid + 1  # Exclude mid b/c it's not minimum
            # [mid, right] is sorted
            else:
                right = mid    # Mid could be minimum
        
        return nums[left]

        # 2. Binary search to compare with left (tracking running min on mid point)
        # left, right = 0, len(nums) - 1
        # res = nums[0]

        # while left <= right:
        #     # If sorted
        #     if nums[left] < nums[right]:
        #         res = min(res, nums[left])
        #         break
            
        #     mid = (left + right) // 2
        #     res = min(res, nums[mid])

        #     # Check which portion (small or large) does mid in
        #     # 1. in large portion (left)
        #     if nums[mid] >= nums[left]:
        #         left = mid + 1
        #     # 2. in small portion (right)
        #     else:
        #         right = mid - 1
        
        # return res



