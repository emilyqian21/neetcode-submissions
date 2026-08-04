"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # edge case
        if not intervals:
            return True
        #sort and detect overlap
        intervals.sort(key = lambda x : x.start) # here class is interval, self.start, slef.end
        preend = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < preend: # overlap
                return False
            preend = interval.end
        return True