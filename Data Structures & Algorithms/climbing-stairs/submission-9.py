class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        #edge case
        if n == 0:
            return 1
        if n == 1:
            return 1
        # base case
        dp[1] = 1
        dp[2] = 2
        print(dp)
        print(dp[-1])
        #main logic
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2] # dp[i] means num of distnct ways to get to stair i
        return dp[-1]
