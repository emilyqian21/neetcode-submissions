"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # time: O(nlogn) ---> sorting
        # space: O(n) ---> heap
        #edge case
        if not intervals:
            return 0
        
        heap = []
        intervals.sort(key = lambda x: x.start)
        heapq.heappush(heap, intervals[0].end) # rank by the end time 

        for interval in intervals[1:]:
            if heap and interval.start < heap[0]: # overlap
                heapq.heappush(heap, interval.end) # start a new room
            else:
                heapq.heappop(heap) # reuse the room. so drop the room fist
                heapq.heappush(heap, interval.end) # update the room info
        return len(heap) 