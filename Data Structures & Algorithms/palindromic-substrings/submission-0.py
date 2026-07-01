class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #odd
            l = i
            r = i 

            while l >= 0 and r < len(s) and s[l] == s[r]:
                #find palindrome
                res += 1
                l -= 1
                r += 1

            #even
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                #find palindrome
                res += 1
                l -= 1
                r += 1
        return res