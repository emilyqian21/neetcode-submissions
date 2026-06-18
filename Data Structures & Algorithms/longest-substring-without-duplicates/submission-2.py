class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        pos_map = {}

        l = 0
        r = 0

        while r < len(s):
            # check if there's duplicate
            if s[r] in pos_map:
                l = max(l,pos_map[s[r]] + 1) # example:[a,b,b,a], l不能后退
                pos_map[s[r]] = r
            
            else:
                pos_map[s[r]] = r 
            cur_len =  r-l + 1
            max_len = max(cur_len, max_len) 
            r += 1
            
        return max_len

        #time: O(n) n = length of the string
        #space: O(m) m = unique characters in the string