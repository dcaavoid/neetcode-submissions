class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search: check if mid is the target.
        # [3, 4, 5, 6, 1, 2], target = 3
        # Check if mid is in whether the left or the right portion.
        # If mid is in the left, compare between left pointer and target:
        #   1. If target < nums[left], search the right portion of mid;
        #   2. If nums[left] <= target < nums[mid], search the left portion of mid.
        # If the mid is in the right porition, compare between right pointer and the target:
        #   1. If target > nums[right], search the left portion of mid;
        #   2, If nums[mid] < target <= nums[right], search the right portion of mid.
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # When mid is in the left portion:
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:   # When mid is in the right portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1