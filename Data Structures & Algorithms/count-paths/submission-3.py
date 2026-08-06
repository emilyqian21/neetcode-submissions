class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time: O(m *n)
        # space: O( m * n) # optimized version can be O(n)
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1 # dp[i] = num of ways to reach that position

        # for i in range(m):
        #     for j in range(n):
        #         if i == j == 0: # if it's [0][0]
        #             continue # we already set dp[0][0] to 1
        #         if i > 0:
        #             dp[i][j] += dp[i - 1][j]
        #         if j > 0:
        #             dp[i][j] += dp[i][j - 1]
        # return dp[-1][-1]


        # optimized version
        # time:O( m * n)
        # space:O(n)
        dp = [1]*n 
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1] +dp[j] # left value + up value. left value is already updated for this row, up value is still the old, not updated value for the above row
        return dp[-1]