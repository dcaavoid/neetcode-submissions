class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic programming with states
        # If buying: i + 1
        # If selling: i + 2 b/c cooldown
        dp = {}    # key=(i, buying (True for buy, False for sell)), val=max profit

        # Starting on day i with(True) or without(False) coins, what's the max profit?
        def dfs(i: int, buying: bool):
            # Base case
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Recursive: either choose buy/sell or cooldown
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        dfs(0, True)
        return dp[(0, True)]