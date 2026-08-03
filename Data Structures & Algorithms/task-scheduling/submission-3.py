class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap --> store counts
        # queue --> when to process same task

        cnt = Counter(tasks)
        maxheap = [ -1*v for v in cnt.values()]
        heapq.heapify(maxheap)

        q = deque() # (cnt, time) # if time = time, add back to maxheap
        time = 0 

        while maxheap or q:
            time += 1
            # update the count in the maxheap
            if maxheap:
                new_cnt = heapq.heappop(maxheap) + 1
                if new_cnt:
                    q.append((new_cnt, time + n))

            if q and q[0][1] == time: # time to add the task to the maxheap to process the task
                taskcnt = q.popleft()[0]
                heapq.heappush(maxheap, taskcnt) # cur_cnt = -3, --> -3+1 = -2 
        return time
