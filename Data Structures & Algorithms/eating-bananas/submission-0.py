class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The range of k is [1, max(piles[i])], given h >= len(piles).
        # Use binary search on the range of k:
        # If mid(k) satisifies the h, try smaller portion of k;
        # If mid(k) rate takes longer time than h, try larger portion of k.

        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            time = 0
            
            # Count the number of hours for current mid k
            for p in piles:
                time += math.ceil(p / mid)
            
            # If time <= h, try smaller k
            if time <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res