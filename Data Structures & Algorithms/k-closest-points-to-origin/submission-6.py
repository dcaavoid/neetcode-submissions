class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # For distance, do not need sqrt b/c if a^2 > b^2, then sqrt(a^2) > sqrt(b^2).
        # Use a tuple to store (dist, coord) pair.
        # Use max heap of size k with (-dist, [x, y]).
        # Pop the current farthest coordinate in O(log(k)) time.
        # Time: O(n*log(k)) for pushing and popping n elements into maxheap of size k;
        # Space: O(k) for keep the k closest elements in a max heap.
        res = []
        maxHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)

            # Push coordinates if there are less than k elements.
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, x, y))
            # Or push coordinates if it's closer to origin than the top coordinate in max heap.
            else:
                farthestDist = -maxHeap[0][0]
                
                if dist < farthestDist:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist, x, y))
        
        for _, x, y in maxHeap:
            res.append([x, y])
        
        return res