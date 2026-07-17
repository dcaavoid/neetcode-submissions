# Find median -> two heaps
# Max heap for left sorted portion, min heap for the right sorted portion
# For any number, first append to the max heap;
# Then make sure numbers in max heap always <= min heap;
# and then make sure len(maxHeap) - len(minHeap) <= 1.
# If there are odd numbers: return top value in max heap;
# If there are even numbers: return average of top values in max and min heap.

class MedianFinder:

    def __init__(self):
        self.maxHeap = []   # Left sorted portion
        self.minHeap = []   # Right sorted porition
    
    # [1, 3, 6, 7, 8]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)

        if (self.minHeap and self.maxHeap and
            -1 * self.maxHeap[0] > self.minHeap[0]):
            temp = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
        
        # Make sure two heaps are balanced in size.
        # 1. more elements in max heap (more smaller num):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            temp = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
        # 2. more elements in min heap (more larger num):
        if len(self.minHeap) - len(self.maxHeap) > 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * temp)
        

    def findMedian(self) -> float:
        # Odd size
        if (len(self.maxHeap) + len(self.minHeap)) % 2:
            if len(self.maxHeap) > len(self.minHeap):
                return (-1 * self.maxHeap[0])
            else:
                return self.minHeap[0]
        # Even size
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2