class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window (varied size): move the right pointer until all letters appear;
        # Then move the left pointer to get shortest valid substring.
        # Special case: return empty string if s is shorter than t.
        if len(s) < len(t):
            return ""

        # Build a hash map to track frequency of letters in t.
        countS, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)

        # Sliding window (varied size)
        # Move right pointer to the right to update the freq of letter from t in substring of s.
        left = 0
        res = [-1, -1]
        resLen = float('inf')
        for right in range(len(s)):
            if s[right] in countT:
                countS[s[right]] = 1 + countS.get(s[right], 0)
                if countT[s[right]] == countS[s[right]]:
                    have += 1

                    # If substring has enough letter, save the temp result and shrink the substring with left pointer.
                    while have == need:
                        if right - left + 1 < resLen:
                            res = [left, right]
                            resLen = right - left + 1
                        
                        if s[left] in countT:
                            countS[s[left]] -= 1
                            if countS[s[left]] < countT[s[left]]:
                                have -= 1
                        
                        left += 1
        left, right = res
        return s[left: right + 1]


        
        