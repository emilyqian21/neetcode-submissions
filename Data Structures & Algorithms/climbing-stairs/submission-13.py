class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {0: 1, 1: 1}
        # def dfs(n):
        #     # return the minial steps to reach step n 
        #     if n in memo:
        #         return memo[n]
        
        #     # main logic
        #     cur =  dfs(n - 1) + dfs(n - 2)
        #     memo[n] = cur
        #     return cur
        # return dfs(n)
        dp = [0] * (n + 1) # number of ways to reach step n
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[ i - 2]
        return dp[-1]

