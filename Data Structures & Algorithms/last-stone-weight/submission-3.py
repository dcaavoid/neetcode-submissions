class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use max heap
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, x - y)
        
        return abs(maxHeap[0]) if len(maxHeap) > 0 else 0