class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # time: O(nlogn) # 一次heappop是logn, 要进行N次
        # space: O(n)
        stones = [ -1*i for i in stones]
        heapq.heapify(stones)
        #edge case
        if not stones:
            return 0
        
        while len(stones) > 1:
            first = heapq.heappop(stones) # -8, the largetst abs value
            second = heapq.heappop(stones) # -7, the second largest abs value

            if abs(first) > abs(second):
                new_stone = (abs(first) - abs(second))*(-1)
                heapq.heappush(stones, new_stone)

        if not stones:
            return 0       
        # or stones.append(0)，但我感觉这样写不清楚
        return abs(stones[0])
        