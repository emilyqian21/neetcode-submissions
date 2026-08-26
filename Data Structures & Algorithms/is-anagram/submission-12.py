class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        count_s = {}
        for c in s:
            if c not in count_s:
                count_s[c] = 0
            count_s[c] += 1
        
        for c in t:
            if c not in count_s:
                return False
            if count_s[c] - 1< 0:
                return False
            count_s[c] -= 1
        
        for v in count_s.values():
            if v != 0:
                return False
        return True