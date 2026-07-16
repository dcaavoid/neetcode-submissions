class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Shortest path (Bellman Ford)
        # k stops = k + 1 edges
        # The cost from src to n; if prices[n] == inf, not reachable so far.
        prices = [float('inf')] * n
        prices[src] = 0
        
        # After i iterations, prices[v] represents the minimal cost from src to v with i edges.
        for i in range(k + 1):
            tmpPrices = prices.copy()   # Save min cost in current iteration.

            for s, d, p in flights:
                # Not reachable yet
                if prices[s] == float('inf'):
                    continue
                
                # Find a path with less cost (based on i-1's result)
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float('inf') else -1