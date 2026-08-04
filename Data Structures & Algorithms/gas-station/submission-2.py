class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       # time: O(n)
       # space: O(1)
        # try every position, if total never < 0 then that's the result

        if sum(gas) < sum(cost): # there'll never be a result
            return -1
        
        total = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0 # reset to 0. this position doesn't work
                start = i + 1 # try next position as the start
        
        return start