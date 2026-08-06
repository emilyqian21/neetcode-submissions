class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 # dp[i] = num of ways to reach that position

        for i in range(m):
            for j in range(n):
                if i == j == 0: # if it's [0][0]
                    continue # we already set dp[0][0] to 1
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]