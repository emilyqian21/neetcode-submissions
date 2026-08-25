"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # compare cur interval with the earlest-end room; if overlap, open a new room; no overlap, reuse and update room end info
        # edge case
        if not intervals:
            return 0
            
        intervals.sort(key = lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)

        
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            cur_room_end = heap[0]

            if cur_interval.start < cur_room_end: # conflict/overlap
                heapq.heappush(heap, cur_interval.end) # open a new room
            else: # no overlap, reuse the room
                heapq.heappop(heap)
                heapq.heappush(heap, cur_interval.end) # udpate the room end info

        return len(heap)