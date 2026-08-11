class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        # count_t = {}

        if len(s) != len(t):
            return False

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            if c not in s:
                return False
            count_s[c] -= 1
            if count_s[c] < 0:
                return False
           
        return True

