class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # At each index (r, c), the number of ways = nums of (r+1, c) + nums of (r, c+1).
        # Base case at grid[m-1][n-1] = 1
        # And since only move right or down, the number of ways at last column and at last row = 1.
        dp = [1] * n

        for row in range(m-1):
            newDP = [1] * n
            for col in range(n - 2, -1, -1):
                newDP[col] = newDP[col + 1] + dp[col]
            
            dp = newDP
        
        return dp[0]