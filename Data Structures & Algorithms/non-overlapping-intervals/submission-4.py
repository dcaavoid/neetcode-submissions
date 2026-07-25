class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Brute force: try every possible subset of intervals, and find the subset with max size.
        # Time: O(n^2 * 2^n) as we can choose or not choose the each interval, and comparing takes O(n^2) time.
        # Optimal solution with greedy: sort by the end time, and whenever there is overlap, keep the interval with smaller end time.
        # It's greedy b/c we remove overlapped intervals with larger end time, leaving more space for following intervals.
        intervals.sort(key=lambda x: x[0])    # First sort by start time, and sort by end time if conflicts.
        count = 0
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals), 1):
            # If conflict
            if intervals[i][0] < lastEnd:
                count += 1
                lastEnd = min(lastEnd, intervals[i][1])
            # If no conflict: update the last end time b/c intervals are sorted by end time.
            else:
                lastEnd = intervals[i][1]
        
        return count