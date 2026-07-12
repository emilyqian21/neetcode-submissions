class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case
        if len(s) != len(t):
            return False
        s_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
        for i in range(len(t)):
            s_count[t[i]] = s_count.get(t[i],0) - 1
            if s_count[t[i]] < 0:
                return False
        return True











        # #solution 1 
        # if len(s) != len(t):
        #     return False
        # count_s = [0]*26
        # count_t = [0]*26
        # for c in s:
        #     count_s[ord(c) - ord('a')] += 1
        # for c in t:
        #     count_t[ord(c) - ord('a')] += 1
        
        # return count_s == count_t
        # #time: O(N)
        # #space: O(1)

        # #solution 2
        # if len(s)!= len(t):
        #     return False

        # count_s = {}
        # count_t = {}

        # for c in s:
        #     count_s[c] = count_s.get(c,0) + 1
        # for c in t:
        #     count_t[c] = count_t.get(c,0) + 1
        # return count_s == count_t
        # # #time: O(N)
        # # #space: O(1)

            