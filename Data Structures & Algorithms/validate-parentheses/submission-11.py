class Solution:
    def isValid(self, s: str) -> bool:
        # Stack + hash map
        # Time: O(n), space: O(n)
        stack = []
        mapping = { "{": "}",
                    "[": "]",
                    "(": ")"}
        
        for c in s:
            # If c is open:
            if c in mapping:
                stack.append(c)
            # If c is close:
            else:
                if not stack or c != mapping[stack.pop()]:
                    return False

        return True if not stack else False