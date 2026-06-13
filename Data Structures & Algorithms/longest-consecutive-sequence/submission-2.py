class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        res = 0
        for i in uniq:
            if i-1 not in uniq: #only start with the smallest 
                streak = 1
                while i+1 in uniq:
                    streak += 1
                    i += 1
                res = max(streak, res)
        return res