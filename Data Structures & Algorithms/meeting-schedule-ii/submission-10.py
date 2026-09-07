"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if conflict with the earliest end room---> initiate a new room 
        # if no conflict with the earliest end room ---> reuse the room, and update the end info
        # minheap --> store (end_time ---> always pop the room with smallest end_time
        # return ---> the len of mimnheap --> number of rooms used

        intervals.sort(key = lambda x : x.start)
        heap = []
        # edge case
        if not intervals:
            return 0

        heapq.heappush(heap,intervals[0].end)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur.start < heap[0]: # overlap, need a new room 
                heapq.heappush(heap, cur.end)
            else: # no overlap, reuse the room 
                heapq.heappop(heap)
                heapq.heappush(heap, cur.end)
        return len(heap)

