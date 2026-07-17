class Solution:
    def countSubstrings(self, s: str) -> int:
        # Two pointers
        res = 0

        def expand(left, right):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd length
            expand(i, i)

            # Even length
            expand(i, i + 1)
        
        return res
        