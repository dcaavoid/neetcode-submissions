class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        # 3,4,5,6,1,2, t = 7
        #       l m r
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Check [left, mid] is sorted portion
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # nums[left] > nums[mid]
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
