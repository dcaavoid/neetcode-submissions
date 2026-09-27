class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a minHeap of size k
        minHeap = []
        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                kth = minHeap[0]
                if n > kth:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, n)
                else:
                    continue
        
        return minHeap[0]