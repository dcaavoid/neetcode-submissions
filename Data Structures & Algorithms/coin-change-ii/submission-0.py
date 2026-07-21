class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Version 2: 2D DP
        # dp[i][a]: given coins[i:], the number of combinations to come up a amount.
        # dp[i][a] = dp[i][a - coins[i]] + dp[i-1][a]
        #    0 1 2 3 4
        #  1
        #  2
        #  3 1
        dp = [0] * (amount + 1)

        for i in range(len(coins) - 1, -1, -1):
            newDP = [0] * (amount + 1)
            newDP[0] = 1
            for a in range(1, amount + 1, 1):
                if a - coins[i] >= 0:
                    newDP[a] = dp[a] + newDP[a - coins[i]]
                else:
                    newDP[a] = dp[a]
            
            dp = newDP
        
        return dp[amount]


        # Version 1: DFS: two choices at each node:
        # 1. choose the current coin
        # 2. not choose the current coin and move on
        # Time & Space: O(n*a) where n=number of coins, a=amount
        # cache = {}  # key=(index, curr), value=number of unique combinations

        # # Given coins[index:], what's the number of combination to come up curr amount?
        # def dfs(index, curr):
        #     # Base case:
        #     if curr == amount:
        #         return 1
        #     if index == len(coins) or curr > amount:
        #         return 0
        #     if (index, curr) in cache:
        #         return cache[(index, curr)]
            
        #     # Recursive
        #     cache[(index, curr)] = dfs(index, curr + coins[index]) + dfs(index + 1, curr)
        #     return cache[(index, curr)]
        
        # dfs(0, 0)
        # return cache[(0, 0)]