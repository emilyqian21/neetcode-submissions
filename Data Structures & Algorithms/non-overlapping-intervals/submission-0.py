class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by interval start
        intervals.sort(key = lambda x : x[0])
        count = 0 
        prevend = intervals[0][1]

        for interval in intervals[1:]:
            # if there is overlap
            if interval[0] < prevend: 
                prevend = min(prevend, interval[1]) # remove the bigger end, so update prevend to the smaller end
                count += 1
            else: # no overlap
                prevend = interval[1]
        return count