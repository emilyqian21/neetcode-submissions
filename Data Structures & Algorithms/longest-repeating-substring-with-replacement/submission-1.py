class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        freq = {}
        max_res = 0
        
        while r < len(s):
            # add new element
            freq[s[r]] = freq.get(s[r],0) + 1

            #check if len(s) - most frequent letter frequency < k, if not, we need to contract l 
            while freq and (r-l+1) - max(freq.values()) > k:
                #drop the left character 
                freq[s[l]] -= 1
                l += 1
            cur_len = r - l + 1
            max_res = max(cur_len,max_res)
               # add new element
            r += 1
        return max_res
         
            
            