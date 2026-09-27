class Solution:
    def numDecodings(self, s: str) -> int:
        # Check by digit:
        # one digit number: 1-9
        # two digit number: 1 -> {0 - 9}; 2 -> {0 - 6}
        
        # ============================================================
        # Method 1: backtracking + memorization
        dp = { len(s): 1 }   # number of ways to decode starting s[i:]

        def dfs(i):
            # Base case
            # 1. If searched through all, or s[i:] has searched
            if i in dp:
                return dp[i]
            # 2. Invalid single digit
            if s[i] == "0":
                return 0
            
            # Recursive
            # 1. Use s[i] only
            res = dfs(i + 1)

            # 2. Use s[i: i + 1]
            if (i + 1 < len(s) and (s[i] == "1" or
                                   (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)