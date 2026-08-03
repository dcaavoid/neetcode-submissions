class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window: expand to the right until window - maxFreq > k,
        # and then shrink the window until the condition satisifies again.
        # Time: O(n), space: O(m)
        count = {}    # char: freq
        res = 0
        maxFreq = 0
        l, r = 0, 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res

        # Brute force: for every possible starting position l, expand a window rightward one character at a time;
        # maintain a running character-frequency count and the frequency of the most common character seen so far in that window;
        # a window is valid if window_length - maxFrequency <= k;
        # track the longest valid window across all starting positions.
        # Time: O(n^2), space: O(m)
        # n = len(s)
        # res = 0

        # for l in range(n):
        #     count = {}  # character: frequency
        #     maxFreq = 0
        #     for r in range(l, n, 1):
        #         count[s[r]] = 1 + count.get(s[r], 0)
        #         maxFreq = max(maxFreq, count[s[r]])
        #         window = r - l + 1
                
        #         if window - maxFreq <= k:
        #             res = max(res, window)
        
        # return res