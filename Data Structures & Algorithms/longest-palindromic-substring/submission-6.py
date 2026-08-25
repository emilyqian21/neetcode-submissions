class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 看一下dp

        max_res = 0
        max_str = ""

        for i in range(len(s)):
            # odd palindrome
            l = i 
            r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > max_res:
                    max_res = max(max_res, cur_len)
                    max_str = s[l: r + 1]
                l -= 1
                r += 1

            # even palidrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > max_res:
                    max_res = max(max_res, cur_len)
                    max_str = s[l: r + 1]
                l -= 1
                r += 1

        return max_str