class Solution:
    def countSubstrings(self, s: str) -> int:
        #time: O(N^2) 
        #space: O(1)
        # or you can write (while part as a helper function and call it)
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