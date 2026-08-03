class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 3 cases: before newInterval, overlap newInterval, after newInterval
        res = []
        i = 0 
        n =  len(intervals) 

        while i < n and intervals[i][1] < newInterval[0]: # before new Interval
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]: # overlap
            #merge
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        # after merge all the overlapped intervals
        res.append(newInterval)

        while i < n and intervals[i][0] > newInterval[1]: # after
            res.append(intervals[i])
            i += 1
        
        return res
