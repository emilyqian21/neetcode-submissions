"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #edge case
        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            last_interval = res[-1]

            if cur_interval.start < last_interval.end: # overlap
                return False
            res.append(cur_interval)
        return True