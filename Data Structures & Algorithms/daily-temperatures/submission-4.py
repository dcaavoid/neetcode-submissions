class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Implement min heap
        # (38, 1), (30, 2)
        # v = 36, i = 3
        # res = [1, 0, 0, 0, 0, 0, 0]
        # Time: O(n log n)
        # Space: O(n) with output, or O(log n) without output
        minHeap = []    # (temperature, index)
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            # Check current is a higher temperature
            while minHeap and minHeap[0][0] < temp:
                _, j = heapq.heappop(minHeap)
                res[j] = i - j
            
            heapq.heappush(minHeap, (temp, i))
        
        return res