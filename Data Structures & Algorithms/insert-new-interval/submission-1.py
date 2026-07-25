class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # No overlap (interval[i] = [start, end], newInterval = [newStart, newEnd])
        # 1. If end < newStart, current interval comes before newInterval;
        # 2. If start > newEnd, newInterval comes before current interval;
        # Overlap:
        # 3. If end >= newStart and start <= newEnd, there is overlap,
        #    update newInterval[0] = min(newStart, start), newInterval[1] = max(newEnd, end)
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            # No overlap check:
            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        res.append(newInterval)
        return res
            