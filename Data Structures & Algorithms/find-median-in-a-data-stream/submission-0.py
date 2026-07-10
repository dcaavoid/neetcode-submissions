# Use max heap (smaller portion) and min heap (larger portion) to retrieve medium in O(1) time.
# Also sorting in a heap takes O(log(N)) time.

class MedianFinder:

    def __init__(self):
        self.maxHeap = []   # Left smaller portion in a sorted array (negative numbers).
        self.minHeap = []   # Right larger portion in a sorted array.            

    def addNum(self, num: int) -> None:
        # By default, add num to max heap (left portion in a sorted array).
        heapq.heappush(self.maxHeap, -1 * num)

        # 1. Every value in max heap <= to every value in min heap;
        if (self.maxHeap and self.minHeap and
            (-1 * self.maxHeap[0]) > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        # 2. The difference between the size of max heap and min heap is less or equal to 1.
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

    def findMedian(self) -> float:
        # If a list is in odd length, find the heap with larger size first, and then get the top value from the heap.
        if (len(self.maxHeap) + len(self.minHeap)) % 2:
            return (-1 *self.maxHeap[0]) if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        # If a list is in even length, the the average of the max from max heap and min from min heap;
        else:
            return ((-1 * self.maxHeap[0]) + self.minHeap[0]) / 2

        