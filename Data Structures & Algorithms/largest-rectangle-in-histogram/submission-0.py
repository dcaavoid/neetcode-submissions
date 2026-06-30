class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # The width in heights[i] is bounded by the first shorter height on both i's left and right.
        # Build monotonic increasing stack with both index and height
        stack = []  # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start, h))

        # Calculate the area of some heights that extends to the end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea