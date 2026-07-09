class Solution:
    # time: O(number of tasks)
    # space: O(1), bc we have at most 26 different tasks
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        maxheap = [ -1 * c for c in cnt.values()]
        heapq.heapify(maxheap) # [-3,-1,-1]

        q = deque() # (cnt, time)
        time = 0

        while maxheap or q:
            time += 1

            if maxheap:
                cur_cnt = heapq.heappop(maxheap) + 1
                if cur_cnt != 0:
                    q.append((cur_cnt, time + n )) # when time become available to process
            #if time is the same as the first element in q, then add back to maxheap
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time