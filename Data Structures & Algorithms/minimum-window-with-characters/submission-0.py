class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Intuitive: sliding window, but don't understand what's the condition for updating?
        # Create two hash maps: one for counting the occurence of each letter in t,
        # and the other for counting the occurence of each letter in the substring of s.
        # Expand the window until all letters in t appears in the substring of t, and then start shrinking until the condition failed.
        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # have = how many letters in substring of s have met the count of characters in t.
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float("inf")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            # Start shrinking the window and keep track the shorter substring
            while have == need:
                # First track the shorter substring
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Then move left pointer to the right
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
