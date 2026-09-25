# Kth largest = top value in a size of k minHeap
# Question: is it possible that kth largest doesn't exist?
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
    

    def add(self, val: int) -> int:
        # Add val into minHeap
        heapq.heappush(self.minHeap, val)
        
        # Keep the size of minHeap as k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]