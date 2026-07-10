"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #room 结束时间
        heap = [] #(end time,roomid)

        intervals.sort(key = lambda x: x.start)
        room_id = 1 # start from 1
        
        for i in range(len(intervals)):
            if heap:
                latest_room_time,latest_room_id= heap[0][0], heap[0][1] # smallest end time 
                if latest_room_time <= intervals[i].start: # the room has meeting ends before the new interval start, reuse the room 
                    latest_room_time, latest_room_id = heapq.heappop(heap)
                    heapq.heappush(heap,(intervals[i].end,latest_room_id))
                else: # no room available, create a new room 
                    room_id += 1
                    heapq.heappush(heap, (intervals[i].end, room_id))
            else:
                heapq.heappush(heap,(intervals[i].end, room_id))
        
        return len(heap)

        