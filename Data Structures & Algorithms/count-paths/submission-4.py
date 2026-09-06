class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # definition: dp [i][j] = uniq paths to get to grid[i][j]
        # main logic: dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 左边 + 上边

        dp = [[0] * n for _ in range(m)] # dp [i][j] = uniq paths to get to grid[i][j]
        dp[0][0] = 1
        # base case
        for j in range(0, n):
            dp[0][j] = 1
        for i in range(0, m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
