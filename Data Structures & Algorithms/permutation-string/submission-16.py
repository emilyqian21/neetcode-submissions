class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed window size, have == required
        #edge case
        if len(s1) >len(s2):
            return False

        s1_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
       

        s2_count = {}
        for c in s2[0:len(s1)]:
            s2_count[c] = s2_count.get(c, 0) + 1
        
        have = 0
        required = len(s1_count) #易错点！！！ 不是len(s1),而是s1.keys()!!!
        for k in s1_count:
            if k in s2_count and s1_count[k] == s2_count[k]:
                have += 1

        if have == required:
            return True
        
        l = 0
        for r in range(len(s1), len(s2), 1):
            # add right and delete left. keep window size fixed

            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            
            if s2[r] in s1_count and s2_count[s2[r]] - 1 == s1_count[s2[r]]:
                have -= 1
            if s2[r] in s1_count and s2_count[s2[r]] == s1_count[s2[r]]:
                have += 1

            s2_count[s2[l]] = s2_count.get(s2[l], 0) - 1
            if s2[l] in s1_count and s2_count[s2[l]] + 1 == s1_count[s2[l]]:
                have -= 1
            if s2[l] in s1_count and s2_count[s2[l]] == s1_count[s2[l]]:
                have += 1

            l += 1

            # test if have == required
            if have == required:
                return True

        return False