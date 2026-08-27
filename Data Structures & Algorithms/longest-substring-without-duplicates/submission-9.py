class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastpos = {}
        l = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i]  in lastpos:
                l = max(l, lastpos[s[i]] + 1)
                
            lastpos[s[i]] = i
            maxlen = max(maxlen, (i - l + 1))

        return maxlen