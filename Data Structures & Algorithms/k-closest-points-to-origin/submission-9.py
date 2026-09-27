import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maxHeap with size of k: (-dist, x, y)
        res = []    # Save each coordinate as a list
        maxHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-1 * dist, x, y))
            else:
                farthestDist = -1 * maxHeap[0][0]
                if dist < farthestDist:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-1 * dist, x, y))
        
        for _, x, y in maxHeap:
            res.append([x, y])
        
        return res