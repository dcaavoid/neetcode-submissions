class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Use each index i as the center, and then expand in two directions.
        # For palidromes, there are both even and odd length.
        res = ""
        resLen = 0

        def expand(left: int, right: int):
            nonlocal res, resLen
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd length:
            expand(i, i)
            
            # Even length:
            expand(i, i + 1)
        
        return res
