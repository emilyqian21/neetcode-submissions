class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] means if s[i:j + 1] is palidromic or not, last character is j 
        # main logic: dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        # base case: if i == j, dp[i][j] = True; if i + 1 == j, dp[i][j] = s[i] == s[j]

        max_len = 0
        max_str = ""
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        # base case
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                if i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                    
                if dp[i][j] == True and (j - i + 1) >= max_len:
                    max_len = max(max_len, j - i + 1)
                    max_str = s[i: j + 1]
        
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n, 1):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] == True and (j - i + 1) >= max_len:
                    max_len = max(max_len, j - i + 1)
                    max_str = s[i: j + 1]

        return max_str