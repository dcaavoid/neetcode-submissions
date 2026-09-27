class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Two heaviest -> maxHeap (negative weights)
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -1 * s)
        
        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, -1 * (x - y))
        
        return -1 * maxHeap[0] if len(maxHeap) > 0 else 0