class Solution:
    def checkValidString(self, s: str) -> bool:
        # Version 3: Greedy
        # Trach the max and min possible number of left parenthesis.
        # If leftMax ever < 0, return false b/c there is more right than left;
        # If leftMin < 0, reset to 0.
        leftMax, leftMin = 0, 0
        for c in s:
            if c == "(":
                leftMax += 1
                leftMin += 1
            elif c == ")":
                leftMax -= 1
                leftMin -= 1
            else:
                leftMax += 1
                leftMin -= 1
            
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0

        # Version 2: dfs with dp to optimimze
        # Time: O(n^3) (But why n^3?); space: O(n^2)
        # cache = {}   # key=(i, openCount), value=boolean

        # def dfs(i, openCount) -> bool:
        #     # Base case
        #     if openCount < 0:
        #         return False
        #     if i == len(s):
        #         return openCount == 0
        #     if (i, openCount) in cache:
        #         return cache[(i, openCount)]
            
        #     # Recursive
        #     if s[i] == "(":
        #         res = dfs(i + 1, openCount + 1)
        #     elif s[i] == ")":
        #         res = dfs(i + 1, openCount - 1)
        #     else:
        #         res = (dfs(i + 1, openCount + 1) or
        #                 dfs(i + 1, openCount - 1) or
        #                 dfs(i + 1, openCount))
        #     cache[(i, openCount)] = res
        #     return res
        
        # return dfs(0, 0)

        # Brute force: dfs: for "*", treat like a decision tree with tree paths: "(", "", or ")".
        # At any point, a valid parenthesis is number of "(" >= number of ")".
        # Time: O(3^n) as there are 3 choices for each *.
        # From index i in s and number of "(", can we form valid  parenthesis?
        # def dfs(i, openCount) -> bool:
        #     # Base case
        #     if openCount < 0:
        #         return False
        #     if i == len(s):
        #         return openCount == 0
            
        #     # Recursive
        #     if s[i] == "(":
        #         return dfs(i + 1, openCount + 1)
        #     elif s[i] == ")":
        #         return dfs(i + 1, openCount - 1)
        #     else:
        #         return (dfs(i + 1, openCount + 1) or
        #                 dfs(i + 1, openCount - 1) or
        #                 dfs(i + 1, openCount))
        
        # return dfs(0, 0)
