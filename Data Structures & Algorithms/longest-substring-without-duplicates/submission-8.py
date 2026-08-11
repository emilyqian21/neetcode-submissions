class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        n = len(s)
        l = 0
        max_len = 0

        for r in range(n):
            c = s[r]
            if c in last_pos: # duplicate
                l = max(l, last_pos[c] + 1)
                last_pos[c] = r
            
            else: # first time see it, record the position
                last_pos[c] = r
    
                
            # record the ans
            cur_len = r - l + 1
            max_len = max(max_len, cur_len)

        return max_len