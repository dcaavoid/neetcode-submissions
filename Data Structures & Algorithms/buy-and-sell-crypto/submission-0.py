class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force: for each price p starting from the beginning,
        # traverse through all the following prices to try max profit.
        # Time: O(n^2)
        # Better solution: two pointers
        # First pointer: track the time to buy
        # Second pointer: track the time to sell
        # if prices[p1] > prices[p2], p1 = p2, p2 += 1
        # if prices[p1] < prices[p2], res = max(res, prices[p2], prices[p1])
        if len(prices) == 1:
            return 0
        
        res = 0
        left, right = 0, 1
        while left < len(prices) - 1 and right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                res = max(res, prices[right] - prices[left])
                right += 1
        
        return res
