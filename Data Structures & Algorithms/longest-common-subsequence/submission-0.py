class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D DP dp[text1][text2] = number of characters matched
        # If text1[i] = text2[i], dp[i][i] = 1 + dp[i+1][i+1] b/c need to check matching in following strings;
        # If text1[i] != text2[i], dp[i][i] = max(dp[i+1][i], dp[i][i+1]) b/c either strings can form longest.
        # Spatial complexity of optimization: save last and current row of array.
        #.    c a t
        #.  c
        #   r
        #   a
        #   b
        #   t
        #dp:  0 0 0 0
        ROWS, COLS = len(text1), len(text2)
        dp = [0] * (COLS + 1)

        for r in range(ROWS - 1, -1, -1):
            newDP = [0] * (COLS + 1)
            for c in range(COLS - 1, -1, -1):
                # If two characters match:
                if text1[r] == text2[c]:
                    newDP[c] = 1 + dp[c + 1]
                # If two characters don't match:
                else:
                    newDP[c] = max(dp[c], newDP[c + 1])
            
            dp = newDP
        
        return dp[0]