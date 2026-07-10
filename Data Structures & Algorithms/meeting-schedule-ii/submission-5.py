"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # time: O(nlogn)
        # space: O(n)
        heap = []
        intervals.sort(key = lambda x: x.start)

        for interval in intervals:
            if heap and interval.start >= heap[0]: # no overlap
                heapq.heappop(heap) # reuse the room
            heapq.heappush(heap, interval.end) # 不论要不要reuse，都要把interval end push 进去
        return len(heap)

        # #room 结束时间
        # heap = [] #(end time,roomid)

        # intervals.sort(key = lambda x: x.start)
        # room_id = 1 # start from 1
        
        # for i in range(len(intervals)):
        #     if heap:
        #         latest_room_time,latest_room_id= heap[0][0], heap[0][1] # smallest end time 
        #         if latest_room_time <= intervals[i].start: # the room has meeting ends before the new interval start, reuse the room 
        #             latest_room_time, latest_room_id = heapq.heappop(heap)
        #             heapq.heappush(heap,(intervals[i].end,latest_room_id))
        #         else: # no room available, create a new room 
        #             room_id += 1
        #             heapq.heappush(heap, (intervals[i].end, room_id))
        #     else:
        #         heapq.heappush(heap,(intervals[i].end, room_id))
        
        # return len(heap)

        