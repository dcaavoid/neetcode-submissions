class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use max heap
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap) * (-1)
            y = heapq.heappop(maxHeap) * (-1)

            if x != y:
                heapq.heappush(maxHeap, abs(x - y) * (-1))
        
        return maxHeap[0] * (-1) if len(maxHeap) > 0 else 0