class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window + hash map
        if len(t) > len(s):
            return ""

        # First create a hash map to count the number of each character in t,
        countT, windowS = {}, {}
        res, resLen = [-1, -1], float("inf")

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # then expand the window until the number of unique type of characters in substring of s match t,
        have, need = 0, len(countT)
        left = 0
        for right in range(len(s)):
            windowS[s[right]] = 1 + windowS.get(s[right], 0)

            if s[right] in countT and countT[s[right]] == windowS[s[right]]:
                have += 1

                # before shrinking, keep updating the minimun length of substring
                # then shrink the window until the previous condition is no longer satisfied
                while have == need:
                    if (right - left + 1) < resLen:
                        res = [left, right]
                        resLen = right - left + 1
                    
                    windowS[s[left]] -= 1
                    # Update only if the count in the substring of s is less than count of chars in t.
                    if s[left] in countT and windowS[s[left]] < countT[s[left]]:
                        have -= 1
                    left += 1
            
        left, right = res
        return s[left: right + 1]


