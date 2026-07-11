class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
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