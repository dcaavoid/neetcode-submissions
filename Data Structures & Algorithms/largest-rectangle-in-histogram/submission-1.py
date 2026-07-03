class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Area = width * height, where width = difference in index, height = shortest among its left and right neighbors.
        # Use monotonic increasing stack to store (index, height)
        # For a new (index, height) pair, pop out any higher height;
        # While popping each pair out, calculate to see if it's potential max area;
        # Once all the (index, height) pairs are popped into stack once, then traverse the stack again to check the area of these increasing heights.
        # [2, 3, 1]
        # [1, 2, 3]
        # [4, 3, 2, 1]
        
        maxArea = 0
        total = len(heights)
        stack = []  # (index, height)
        
        # First create a monotonic increasing stack
        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea, height * (i - index))
            
            # Since pop out any taller heights, the width of shorter height should start from the left most taller height.
            stack.append((start, h))
        
        # Then iterate the monotonic increasing stack to find any potential max area.
        for i, h in stack:
            maxArea = max(maxArea, h * (total - i))
        
        return maxArea
            
