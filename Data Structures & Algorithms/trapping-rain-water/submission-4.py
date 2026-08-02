class Solution:
    def trap(self, height: List[int]) -> int:
        # Optimal solution: two pointers to track the bounds.
        # Update pivot to the bound with smaller bound b/c it's the bottle-neck of min(leftBound, rightBound).
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        
        return res

        # ---------------------------------------------------------------
        # Brute force: for each index, find the left and right bound, and then calculate the amount of water trapped.
        # Time: O(2n) ~ O(n), space: O(2n) ~ O(n)
        # n = len(height)
        # leftBound = [0] * n
        # leftBound[0] = height[0]
        # rightBound = [0] * n
        # rightBound[n - 1] = height[n - 1]
        # res = 0
        

        # # Get left bound of each index
        # for i in range(1, n):
        #     leftBound[i] = max(height[i], leftBound[i - 1])
        
        # # Get right bound of each index
        # for i in range(n - 2, -1, -1):
        #     rightBound[i] = max(height[i], rightBound[i + 1])
        
        # # Calculate trapped water
        # for i in range(n):
        #     res += (min(leftBound[i], rightBound[i]) - height[i])
        
        # return res