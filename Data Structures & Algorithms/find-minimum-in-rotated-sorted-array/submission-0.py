class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Use binary search, but don't understand the condition to get rid of one half.
        # Since the array is rotated, we know two portions of the arrays are sorted.
        # Two versions:
        # # Version 1. compare nums[mid] with nums[right] to search the min within left anf right bound.
        # left, right = 0, len(nums) - 1

        # # Use left < right b/c when left == right, we find the min value.
        # while left < right:
        #     mid = (left + right) // 2
            
        #     # In a valid portion, nums[mid] will never greater than nums[right].
        #     # If this is true, the break point is in the right porition.
        #     # Since nums[mid] > nums[right], nums[mid] can never be the min value,
        #     # so left = mid + 1 to skip this value.
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         # If nums[mid] <= nums[right] (but mid never equal to right b/c mid calculation),
        #         # mid-right portion is sorted, aand mid could be the min value b/c mid is the currently smallest value within mid-right portion.
        #         right = mid
        
        # return nums[left]

        # ----------------------------------------------------------------------------
        # Version 2. compare nums[mid] with nums[left].
        res = nums[0]   # ?
        left, right = 0, len(nums) - 1

        # Use <= to make sure every possible value is checked.
        while left <= right:
            # Quickly find the min in a sorted array
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            # Record every possible number b/c we skip mid while updating left and right pointers.
            mid = (left + right) // 2
            res = min(res, nums[mid])

            # If nums[mid] >= nums[left], left-mid porition is sorted.
            # Use >= b/c mid could equal to left.
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # If nums[mid] < nums[left], mid is on the right of the break point, so search its left.
                right = mid - 1
        
        return res
