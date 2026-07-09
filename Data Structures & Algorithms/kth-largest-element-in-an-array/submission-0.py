class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap with size k element
        # Push into heap only if: (1) less than k elements; (2) top value is less than current value.
        minHeap = []

        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                minNum = minHeap[0]
                if num > minNum:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num)
        
        return minHeap[0]

