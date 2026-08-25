class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:x[0]) # sort by start
        preend = intervals[0][1]

        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if cur_interval[0] < preend: # overlap
                count += 1
                preend = min(cur_interval[1], preend) # keep the smaller end, remove the larger end
            else:
                preend = cur_interval[1]
        return count