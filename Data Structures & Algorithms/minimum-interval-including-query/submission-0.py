class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort + minheap

        # 1. sort the intervals by start 
        intervals.sort(key = lambda x: x[0])
        
        # 2. make a copy of sorted queries(we need to original queries to know the output order)
        copy_queries = sorted(queries)
        res = {} # save the answer for each q {q: answer}

        # 3. for each query, traverse all possible intervals. remove the invalid intervals and pop the smallest interval length as answer
        heap = []
        i = 0
        for query in copy_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                interval_len = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap,(interval_len, intervals[i][1])) # if tie, use the interval with smaller end
                i += 1
            
            # remove the invalid interval
            while heap and heap[0][1] < query: # heap[0] can be our answer so we need to check if it's valid. if the interval end smaller than query, then it's invalid
                heapq.heappop(heap)


            # now everything in the heap (if there is heap) is valid
            if heap:
                res[query] = heap[0][0] 
            else:
                res[query] = -1
        
        # now we have run all the queries. we need to map it back to the original order
        return [ res[q] for q in queries]