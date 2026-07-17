class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed window problem, hashmap as count, and sliding window

        # edge case
        if len(s2) < len(s1):
            return False
        
        # intialize the first fixed window
        s1_count = collections.Counter(s1)
        s2_count = collections.Counter(s2[:len(s1)])
        match = 0
        l = 0
        # initialize the match
        for i in s1_count:
            if i in s2_count and s1_count[i] == s2_count[i]:
                match += 1
     
        # sliding window on s2 
        for r in range(len(s1),len(s2)):
            # check at the beginning
            if match == len(s1_count):
                return True

            # expand the right side
            c2 = s2[r]
            s2_count[c2] = s2_count.get(c2,0) + 1
            # update the match
            if c2 in s1_count and s2_count[c2] == s1_count[c2]:
                match += 1
            elif c2 in s1_count and s2_count[c2] == s1_count[c2] + 1: # broke the match 
                match -= 1
            
            # shrink the left side to make sure the window size is fixed
            c = s2[l]
            s2_count[c] = s2_count.get(c,0) - 1
            # update the match 
            if c in s1_count and s2_count[c] == s1_count[c]: # find a match
                match += 1
            elif c in s1_count and s2_count[c] + 1 == s1_count[c]: # it was equal before, now it's not
                match -= 1
            l += 1

        return match == len(s1_count)



