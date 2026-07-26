class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Brute force: for each query iterate through the intervals.
        res = []
        for q in queries:
            curMin = float('inf')
            for i in intervals:
                if q >= i[0] and q <= i[1]:
                    curMin = min(curMin, i[1] - i[0] + 1)
            
            if curMin == float('inf'):
                curMin = -1
            
            res.append(curMin)
        
        return res
