"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # detect if there is overlap
        intervals.sort( key = lambda x : x.start)
        #edge case
        if not intervals:
            return True

        res = [intervals[0]]

        for interval in intervals[1:]:
            prev = res[-1]
            if interval.start < prev.end and prev.start < interval.end: # overlap
                return False
            res.append(interval)
        return True 

        
