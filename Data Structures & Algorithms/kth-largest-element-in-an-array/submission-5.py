class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Two versions:
        # Verion 1: min heap of size k: if size > k, pop smallest value.
        # How to heapify first?
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

        # Time: O(N*logK); space: O(K)
        # Version 2: Quick select