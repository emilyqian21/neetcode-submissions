class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for interval in intervals[1:]:
            prev = res[-1]
            if interval[0] <= prev[1] and prev[0] <= interval[1]: # overlapping
                res[-1] = [min(interval[0], prev[0]), max(interval[1], prev[1])]
            elif interval[0] > prev[1]: # after
                res.append(interval)
        
        return res


            