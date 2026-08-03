class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap

        stones = [-1*s  for s in stones]

        heapq.heapify(stones)
        
        while len(stones) >=2:
            x = -1 * heapq.heappop(stones) # the biggest (with smallest negative value) 5
            y = -1 * heapq.heappop(stones) # the second biggest 4
            if x == y: 
                continue
            else:
                newstone = x - y
                heapq.heappush(stones, -1 * newstone)

        if stones:
            return -1 * stones[0]
        else:
            return 0
            
            # return stones[0] if stones else 0