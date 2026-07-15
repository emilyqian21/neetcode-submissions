class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # results space of k 
        # min of k = 1, max of k = max(piles)

        #pattern: answer has a range
        # solution: binary search, l = smallest valid answer
        # time: O(nlogm),Search range: 1 to max(piles) → O(log m) iterations. In each iteration, find_time(speed) scans every pile once → O(n).
        # space: O(1)
        l = 1
        r = max(piles)
        
        def find_time(s):
            t = 0
            for p in piles:
                   t+= math.ceil(p/s) #2.5 -->3
            return t


        while l <= r:
            m = (l + r)//2
            t = find_time(m)
            if t <= h: # can slow down
                r = m - 1 #r is the largest invalid speed.
            else: # need to speed up
                l = m + 1 #l is the smallest valid speed.
        return l
            