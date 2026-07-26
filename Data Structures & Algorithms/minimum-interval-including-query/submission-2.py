class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Optimal sort the queries, and sort theintervals by start time.
        # Since sorting the queries re-order each number, use a hashmap to reference the query->index.
        # Use a min heap (size, end time) to track valid intervals given current query.
        # For each query, first add any intervals that start time <= query only;
        # then remove any intervals that end time < query;
        # after no more valid intervals for current query, get (not pop) the interval with smallest size and earliest end time.
        intervals.sort(key=lambda x: x[0])   # Sort intervals by start time
        minHeap = []    # (size, end time)
        res = {}    # query -> size
        j = 0     # j: intervals pointer

        for q in sorted(queries):
            # Add intervals to min heap
            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heapq.heappush(minHeap, (r - l + 1, r))
                j += 1
            
            # Remove any intervals that out of bound for queries[i]
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Add result size for each query
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [ res[q] for q in queries ]

        # Brute force: for each query iterate through the intervals.
        # Time: O(m*n)
        # res = []
        # for q in queries:
        #     curMin = float('inf')
        #     for i in intervals:
        #         if q >= i[0] and q <= i[1]:
        #             curMin = min(curMin, i[1] - i[0] + 1)
            
        #     if curMin == float('inf'):
        #         curMin = -1
            
        #     res.append(curMin)
        
        # return res