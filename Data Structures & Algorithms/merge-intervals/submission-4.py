class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x:x[0]) # sort by start

        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last_interval = res[-1]
            cur_interval = intervals[i]

            if cur_interval[0] <= last_interval[1]: # overlap
                res[-1] = [min(cur_interval[0], last_interval[0]), max(cur_interval[1], last_interval[1])]
            else: # no overlap
                res.append(cur_interval)
        return res