class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j] = s[i:j + 1] (last character s[j]) are palindrome or not.

        maxlen = 0
        res = ""
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i, len(dp), 1):
                if i == j:
                    dp[i][j] = True
                else:
                    if i == j - 1:
                        dp[i][j] = (s[i] == s[j])
                    else: 
                        dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

                if dp[i][j]:
                    if (j - i +1) > maxlen:
                        maxlen = max(maxlen, j - i +1)
                        res = s[i: j + 1]
              
        return res