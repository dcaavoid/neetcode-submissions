class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search on every possible mid point to find min.
        # Since array is rotated, first find if the mid is in the left or right portion.
        # If mid >= left (use equal b/c mid = (left + right) // 2 might equal to left), it's in the left sorted portion,
        # so left = mid + 1.
        # If mid < left, it's in the right portion, so right = mid - 1.
        # Check res = min(res, nums[mid]) every step.
        left, right = 0, len(nums) - 1
        # Start with nums[0] b/c it's a valid number in nums, and through later min comparison, we are going to find the valid min.
        # res is valid iff res <= min(nums).
        res = nums[0]

        # Allow left == right for mid to find possible min.
        while left <= right:

            # First check if the whole array is in ascending order
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            res = min(res, nums[mid])
            
            # Left sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:   # Right portion
                right = mid - 1
        
        return res