class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need and have 
        countt = {}
        for c in t:
            countt[c] = countt.get(c, 0) + 1
        
        need = len(countt)
        have = 0

        countwindow = {}
        res = float('inf')
        res_str = ""

        l = 0
        for r in range(len(s)):
            c = s[r]
            countwindow[c] = countwindow.get(c, 0) + 1

            if c in countt and countwindow[c] == countt[c]:
                have += 1
            # elif c in countt and countwindow[c] - 1 == countt[c]: # 易错点！ 这道题不需要正好等于，只需要>=就可以，所以不需要这一句
            #     have -= 1
    
            while have == need: #valid window
                if (r - l + 1) < res:
                    res = (r - l + 1)
                    res_str = s[l : r + 1]
                # try to shrink
                c2 = s[l]
                countwindow[c2] = countwindow.get(c2, 0) - 1
                if c2 in countt and countwindow[c2] + 1 == countt[c2]:
                    have -= 1
                l += 1

        return res_str