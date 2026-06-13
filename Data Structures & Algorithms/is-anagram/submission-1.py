class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #edge case
        # if len(s)!= len(t):
        #     return False
        
        # count_s = [0]*26
        # count_t = [0]*26

        # for i in range(len(s)):
        #     count_s[ord(s[i]) - ord('a')] += 1
        #     count_t[ord(t[i]) - ord('a')] += 1
        
        # return count_s == count_t

        # #time: O(N)
        # #space: O(1)

        #solution 2
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for letter in s:
            count_s[letter] = count_s.get(letter,0)+ 1
        for letter in t:
            count_t[letter] = count_t.get(letter,0) + 1
        return count_s == count_t

        #time： O（N）
        #space: O (1)