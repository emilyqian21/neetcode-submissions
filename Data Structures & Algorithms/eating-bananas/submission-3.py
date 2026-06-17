class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            mid = l + (r-l)//2 
            time = 0 
            for p in piles:
                time += math.ceil(p/mid)
            
            if time <= h: # acheive the task, time <= required time, still space to reduce speed
                res = mid # mid is the new miminum speed
                r = mid -1 # try to further reduce the speed
            
            else: # time is more than target
                l = mid + 1 # try to further increase the speed
            

        return res
        # time: o( n * logm) n = len of input array, m = maximum pile, 每个k我们都要跑n遍排得到总共的time
        # space: o (1)
        
