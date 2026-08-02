class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force: start building from each character in s and append characters after it until duplicate characters.
        # Time: O(n^2)
        # Sliding window: expand the right pointer until duplicates, and shrink the left pointer until no more duplicate.
        # Use a hash set to track appeared characters.
        # Time: O(n), space: O(n)
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        res = 0
        left, right = 0, 0
        chars = set()

        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                res = max(res, len(chars))
                right += 1
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1

        return res