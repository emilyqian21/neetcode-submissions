class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need, have

        # counter of t
        count_t = collections.Counter(t)
        count_window = {}
        need = len(count_t) # unique characters in t
        have = 0 # match; if have == need, then we found all the characters we need
        res = [-1,-1] # index of the subarray
        res_len = float('inf')
        l = 0 
        for r in range(len(s)):
            count_window[s[r]] = count_window.get(s[r],0) + 1
            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
                have += 1
            while need == have: 
                # record the answer
                if r - l + 1< res_len:
                    res = [l,r]
                    res_len = r - l + 1
                # try to shrink 
                #update have 
                if s[l] in count_t and count_window[s[l]] == count_t[s[l]]:
                    have -= 1
                count_window[s[l]] -= 1
                l += 1
        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""

