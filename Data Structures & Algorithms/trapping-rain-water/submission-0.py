class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers, update left_max and right_max which tracks the max height before index left and max height after index right,
        # and the area[i] = min(left_max, right_max) - heights[left/right].
        # Move the left or right pointer with smaller max height
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            # Always update the pointer with smaller max height (but why)
            # Move the pointer first b/c at the beginning, the end point cannot hold any water.
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]  # Don't need to consider negative case b/c left_max >= height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        
        return res
