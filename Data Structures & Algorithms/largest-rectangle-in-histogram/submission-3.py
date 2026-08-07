class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack (h, i) = (1, 1), (2, 3), (2, 4), (4, 5)
        # h = 2, i = 4
        # res = 7
        # Every time pop: (i - stack[-1][1]) * stack[-1][0]
        # After iterating through all heights, pop from the end,
        # and calculate (len(heights) - stack[-1][1]) * stack[-1][0]
        stack = []   # (height, index) by decreasing order in height
        res = 0

        # First build monotonic decreasing stack in height
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                prevH, j = stack.pop()
                res = max(res, (i - j) * prevH)
                start = j
            
            stack.append((h, start))
        
        # Iterate through stack 
        n = len(heights)
        while stack:
            h, i = stack.pop()
            res = max(res, (n - i) * h)
        
        return res
