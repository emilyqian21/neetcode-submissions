class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers
        longest_len = 0
        res = ""
        #Because every string can contain both odd-length and even-length palindromes,
        # run both odd and even
        # odd
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > longest_len:
                    res = s[l:r+1]
                    longest_len = r-l+1 
                l -= 1 # expand outwards
                r += 1 #expand outwards
        #even 
        for i in range(len(s)):
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > longest_len:
                    res = s[l:r+1]
                    longest_len = r-l+1 
                l -= 1 # expand outwards
                r += 1 #expand outwards
        return res