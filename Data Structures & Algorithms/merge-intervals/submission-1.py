class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Use the first interval to compare with the following interval.
        intervals.sort()
        curr = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > curr[1]:
                res.append(curr)
                curr = intervals[i]
            elif intervals[i][1] < curr[0]:
                res.append(intervals[i])
            else:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
        
        res.append(curr)
        return res
