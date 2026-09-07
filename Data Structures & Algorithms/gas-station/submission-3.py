class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        # main logic: 
                # 总 gas < 总 cost → 一定无解
                # 如果从 start 出发，到 i 时油量变负，那么 start 到 i 之间任何点都不可能是答案，所以直接 start = i + 1
        if sum(gas) < sum(cost):
            return -1
        start = 0 
        total = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            
            if total < 0: # then this can't be the start point. the start point total will never be below 0 
                total = 0 
                start = i + 1
        return start