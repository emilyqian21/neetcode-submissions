class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l (收缩：contract?），跳到
        # r (traverse)
        max_res = 0
        l = 0
        r = 0
        seen = {} # the last time it wil appear
        while r < len(s):# not outbond
            if s[r] in seen: # seen before
                l = max(l,seen[s[r]]+1)
            seen[s[r]] = r
            
            #record answer
            length = r - l + 1
            max_res = max(max_res, length)
            #update r
            r += 1
        return max_res

