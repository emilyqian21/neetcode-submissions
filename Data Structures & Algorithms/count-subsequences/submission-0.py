class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)] # dp[i][j] = the number of ways to form t[:j] using s[:i]

        # base case: there's always 1 way to form t[:0] --> dp[i][0] = 1
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1,n + 1): # dp[0][j] = s[:0] match t[:j] 全等于 0
            for j in range(1, m + 1): # dp[i][0] 已经在base case写了都等于1
                # case 1:  s[i - 1] == t[j - 1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] # if current characters match: ways = ways_if_I_skip_it + ways_if_I_use_it
                else:
                    dp[i][j] = dp[i -1][j] # skip it
        return dp[-1][-1]






#                   t
#         ""   b   a   g
# s  ""   1    0   0   0
#    b    1
#    a    1
#    b    1
#    ...