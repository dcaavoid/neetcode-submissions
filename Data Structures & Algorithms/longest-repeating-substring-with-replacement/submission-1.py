class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hash Map to count the number of occurence of each letter,
        # and use sliding window to track the current longest substring.
        # Move left pointer once length - max_freq > k.
        # Time: O(26 * N) ~ O(N) b/c we need to check the max freq in every iteration.
        # ex. k = 1, ABBAA
        count = {}
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            # Since we move one index a time, we can safely use if
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, (right - left + 1))
        
        return res