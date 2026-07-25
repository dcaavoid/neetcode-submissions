"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # (5,10) (15, 20), (0, 30)
        # (0,8) (9,10), (15,20)
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x.start)
        lastEnd = intervals[0].end

        for i in intervals[1:]:
            if i.start < lastEnd:
                return False
            lastEnd = i.end
        return True