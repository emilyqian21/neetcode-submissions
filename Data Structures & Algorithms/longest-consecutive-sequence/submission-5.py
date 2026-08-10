class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums) 
        res = 0

        for n in uniq:
            cur = n 
            if cur - 1 not in uniq: # start
                streak = 1
                while cur + 1 in uniq:
                    streak += 1
                    cur += 1
                res = max(res, streak)

        return res