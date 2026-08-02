class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force: for each price p starting from the beginning,
        # traverse through all the following prices to try max profit.
        # Time: O(n^2)
        # Better solution: track min price and max profit
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        
        return maxProfit
