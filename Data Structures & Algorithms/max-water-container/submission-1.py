class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force: for each height i starting from the front,
        # iterate through the following heights to try possible max.
        # Time: O(n^2)

        # Better solution: two pointers (start and end)
        # Each time only move the shorter height toward the center to find possible larger height.
        # Time: O(n)
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            res = max(res, curr)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res