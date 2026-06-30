class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use monotonic decreasing stack (store index)
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # If a greater temperature comes, keep popping any temperatures that is smaller in the front.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index

            # If t[i] <= stack[-1], append the current t[i]
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
        
        return res
                
