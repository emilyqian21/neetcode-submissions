class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        
        for c in t:
            if c not in count_s:
                return False
            if count_s[c] - 1 < 0:
                return False
            count_s[c] -= 1
        return True