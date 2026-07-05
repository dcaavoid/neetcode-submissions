class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The array is sorted in two portions -> use binary search
        # Check if mid pointer has the target value.
        # Determine which portion does the mid pointer in:
        # 1. If mid in left portion (nums[mid] >= nums[left]):
        #   a. If target is in the left of mid: right = mid - 1
        #   b. If target is in the right of mid: left = mid + 1
        # 2. If mid in the right portion (nums[mid] < nums[left]):
        #   a. If target is in the left of mid: right = mid - 1
        #   b. If target is in the right of mid: left = mid + 1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Left sorted portion
            if nums[mid] >= nums[left]:
                # Left of mid
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:   # Right of mid
                    left = mid + 1
            else:   # Right sorted portion
                # Right of mid
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:   # Left of mid
                    right = mid - 1
        
        return -1


