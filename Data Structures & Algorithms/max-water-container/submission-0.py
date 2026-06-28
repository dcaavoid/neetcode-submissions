class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initial thought: two pointer, and always move the pointer with smaller height
        left, right = 0, len(heights) - 1
        res = 0
        
        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            res = max(curr, res)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return res