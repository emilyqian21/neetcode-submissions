class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums) 
        res = 0

        for n in uniq:
            if n - 1 not in uniq: # start
                streak = 1
                while n + 1 in uniq:
                    streak += 1
                    n += 1
                res = max(res, streak)
                
        return res