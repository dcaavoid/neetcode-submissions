class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Implement stack
        # Time: O(n), space: O(n)
        stack = []    # index of unresolved temperatures from smallest (top) to largest (bottom)
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            # Check current is a higher temperature
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            
            stack.append(i)
        
        return res