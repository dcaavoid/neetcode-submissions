class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(": ")",
                       "{": "}",
                       "[": "]"}
        
        stack = []

        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if not stack or c != parentheses[stack.pop()]:
                    return False
        
        return True if stack == [] else False