class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand from center
        maxlen = 0
        resstring = ""

        for i in range(len(s)):
            # odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                new_len = r - l + 1
                if new_len > maxlen:
                    maxlen = new_len
                    resstring = s[l:r + 1]
                l -= 1
                r += 1
            
            # even palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                new_len = r - l + 1
                if new_len > maxlen:
                    maxlen = new_len
                    resstring = s[l:r + 1]
                l -= 1
                r += 1
        return resstring
