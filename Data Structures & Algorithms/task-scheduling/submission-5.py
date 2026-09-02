class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap store ready-to-process task frequency
        # queue store waiting-to-process task and available time
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        maxheap = [] # -1 * task freq, pop the largest freq ( smallest  - 1 * freq)
        q = deque([]) # (available time, task freq)

        for task, freq in count.items():
            heapq.heappush(maxheap, -freq)
        
        time = 0

        while maxheap or q: # when there is task remaining
            time += 1
            if maxheap:
                negfreq = heapq.heappop(maxheap) + 1
                # add to heap
                if negfreq: 
                    q.append((time + n, negfreq))
            # process heap
            if q:
                if q[0][0] == time:
                    heapq.heappush(maxheap, q.popleft()[1])
        return time