class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time: O(n)
        # space: O(1)
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count:
                return False

            count[c] -= 1

            if count[c] < 0:
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

            