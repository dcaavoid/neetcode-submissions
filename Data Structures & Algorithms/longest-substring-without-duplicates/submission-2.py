class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initial thought: Hash Set + one pointer
        # Does not resolve: the longest substring does not start from the beginning.
        # Better: Hash Set + two pointers (sliding window)
        # Right pointer: add new elements; left pointer: remove duplicate elements
        # Moves right pointer until there is duplicate in the set, and then move left pointer until there is no duplicate in the sets.
        # Special Case: 0 or 1 element (guarantee at least 2 elements in the following code)
        if len(s) == 0 or len(s) == 1:
            return len(s)

        chars = set()
        res = 0
        left, right = 0, 0

        while right < len(s):
            # If there are new chars to add to current substring
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))
            else:   # If there is a duplicate char
                while left < right and s[right] in chars:
                    chars.remove(s[left])
                    left += 1
        
        return res