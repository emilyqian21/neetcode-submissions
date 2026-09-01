class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap --> store counts of ready-to-process task
        # queue --> store counts of (not-ready-to-process task, ready-time)
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        maxheap = []
        for k, f in count.items():
            maxheap.append(-f)
        heapq.heapify(maxheap)

        q = deque([])

        time = 0
        
        # start to process
        while maxheap or q:
            # process the task with highest frequency
            time += 1
            if maxheap:
                f = heapq.heappop(maxheap) + 1

                if f: # still have remaining frequncy for this task
                    q.append((f, time + n))

            if q and q[0][1] == time:
                newf, _ = q.popleft()
                heapq.heappush(maxheap, newf)
            
        return time