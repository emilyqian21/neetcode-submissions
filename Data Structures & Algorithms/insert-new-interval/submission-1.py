class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        res = []
        i = 0 
        n = len(intervals)
        # first case: left side
        while i < n and intervals[i][1] < new_start: # end < new start
                res.append([intervals[i][0],intervals[i][1]])
                i += 1
        # second case: overlap, 不停 merge overlap
        while i < n and new_start <= intervals[i][1] and intervals[i][0] <= new_end: 
                # 不停merge
                new_start = min(new_start,intervals[i][0] )
                new_end = max(new_end, intervals[i][1])
                i += 1
        # 全都结束了
        res.append([new_start, new_end])

            # overlap
        while i < n and intervals[i][0] >  new_end:
                res.append([intervals[i][0], intervals[i][1]])
                i += 1
            
        
        return res

            