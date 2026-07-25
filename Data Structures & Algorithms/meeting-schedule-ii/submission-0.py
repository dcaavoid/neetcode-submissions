"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Did not figure out how to track the start and end time in each meeting room.
        # min number of meeting rooms = max number of overlap. 
        # Sort start and end time separately:
        # By the time of next meeting starts, has any currently-running meeting already ended?
        start = []   # Sort start time by acsending order
        end = []     # Sort end time by ascending order
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        maxRoom = 0
        room = 0
        i, j = 0, 0     # i: index of start; j: index of j
        while i < len(intervals):
            # By the time of next meeting starts,
            # has any currently-running meeting already ended?
            if start[i] < end[j]:
                room += 1
                maxRoom = max(maxRoom, room)
                i += 1
            else:
                room -= 1
                j += 1
        
        return maxRoom

            