class Solution:
    def climbStairs(self, n: int) -> int:
        # DP: bottom up
        # dp[i]: starting at i, the number of ways to get to n.
        # Base case: dp[n] = 1 b/c it's at the dst.
        # Optimization in space: only define two variables to represent dp[i + 1] and dp[i + 2].
        one, two = 1, 1
        for i in range(n - 1):
            temp = one + two
            two = one
            one = temp
        
        return one