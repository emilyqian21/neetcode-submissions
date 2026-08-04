class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        preend = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0] < preend: # overlap
                res += 1
                preend = min( intervals[i][1], preend)
            else:
                preend = intervals[i][1]
        return res