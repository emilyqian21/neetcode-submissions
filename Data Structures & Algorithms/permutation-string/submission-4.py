class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # valid window condition: all freq = 0， window length fixed and same

        #edge case:
        if len(s1) > len(s2):
            return False
        
        l = 0
        s1_count = collections.Counter(s1)
        s2_count = collections.Counter(s2[:len(s1)]) 
        if s1_count == s2_count:
            return True

        for r in range(len(s1) , len(s2)): #start from len(s1) so the window size always fix at len(s1)
            # add new 
            s2_count[s2[r]] = s2_count.get(s2[r],0) + 1
            # delete old
            s2_count[s2[l]] = s2_count.get(s2[l],0) - 1

            l += 1
            
            if s1_count == s2_count:
                return True
        
        return False

            
            

        