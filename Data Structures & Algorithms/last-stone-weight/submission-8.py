class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # - 5
            second = heapq.heappop(stones) # -3
            if abs(second) < abs(first): # second abs < first abs
                heapq.heappush(stones, first -second) #-((-first) - (-second))

        stones.append(0)
        return abs(stones[0])