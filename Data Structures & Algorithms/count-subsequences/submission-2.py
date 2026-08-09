class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # time: O(m * n)
        # space: O(m * n)
        n = len(s)
        m = len(t)

        # dp[i][j] = number of ways to form t[:j] using s[:i]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case:
        # There is exactly 1 way to form an empty t: choose nothing.
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s[i - 1] == t[j - 1]:
                    # 1. skip s[i-1]
                    # 2. use s[i-1] to match t[j-1]
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

                else:
                    # current s character cannot help
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

#                   t
#         ""   b   a   g
# s  ""   1    0   0   0
#    b    1
#    a    1
#    b    1
#    ...