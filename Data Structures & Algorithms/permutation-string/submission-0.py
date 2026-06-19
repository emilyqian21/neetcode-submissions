class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = 0
        if len(s2) < len(s1):
            return False

        s1_count = [0]*26
        s2_window_count = [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_window_count[ ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_window_count:
            return True

        for r in range(len(s1),len(s2)):
            # add new element
            s2_window_count[ord(s2[r]) - ord('a')] += 1
            # remove old elemnt
            s2_window_count[ord(s2[l]) - ord('a')] -= 1
            l += 1     
             #check window
            if s2_window_count == s1_count:
                return True
     
        return False