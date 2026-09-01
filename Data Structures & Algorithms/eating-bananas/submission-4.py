class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force: start from max piles[i] and then decrement
        # Time: O(m*n) where m is max pile, n is len(piles)
        # Binary search on k:
        # Special case: is it guaranteed to finish all bananas?    
        low, high = 1, max(piles)
        res = 0

        while low <= high:
            mid = (low + high) // 2
            time = 0

            for p in piles:
                time += (p + mid - 1) // mid
            
            if time <= h:
                # Found a valid k, and future k will be strictly smaller than this k.
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res