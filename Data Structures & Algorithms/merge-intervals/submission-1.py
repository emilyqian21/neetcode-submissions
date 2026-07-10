class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time: O(nlogn)
        # space: O(n)
        # sort by start
        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]

        for i in intervals[1:]:
            old_intervals = res[-1] 
            if i[0] <= old_intervals[1] and old_intervals[0] <= i[1]: # overlap
                res[-1] = [min(old_intervals[0], i[0]), max(old_intervals[1], i[1])]
            else:
                res.append(i)
        return res


