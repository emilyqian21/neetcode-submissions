class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap

        stones = [-1*s  for s in stones]

        heapq.heapify(stones)
        
        while stones:
            while len(stones) >= 2:
                x = -1 * heapq.heappop(stones)
                y = -1 * heapq.heappop(stones)

                if x == y:
                    continue
                elif x < y:
                    newstone = y - x
                    heapq.heappush(stones, -1 * newstone)
                else:
                    newstone = x - y
                    heapq.heappush(stones, -1 * newstone)

            if stones:
                return -1 * stones[0]
            else:
                return 0
            
            # return stones[0] if stones else 0