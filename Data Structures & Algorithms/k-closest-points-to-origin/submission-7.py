import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # minHeap: (dist, x, y)
        res = []    # Save each coordinate as a list
        minHeap = []
        for p in points:
            dist = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(minHeap, [dist, p[0], p[1]])
        
        while len(res) != k:
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res