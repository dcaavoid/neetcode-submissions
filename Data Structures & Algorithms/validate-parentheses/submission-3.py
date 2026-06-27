class Solution:
    def isValid(self, s: str) -> bool:
        # special case
        if len(s) % 2 != 0:
            return False
        
        # general case
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in closeToOpen: # left parentheses
                stack.append(c)
            else: # right parentheses
                if not stack or closeToOpen[c] != stack.pop(): # )) case and general case
                    return False
        # (( case
        return True if not stack else False
        
