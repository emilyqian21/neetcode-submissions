class Solution:
    def climbStairs(self, n: int) -> int: #fibonacci
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0]* n
        dp[0] = 1
        dp[1] = 2

        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2] # at position i, the ways to get position i is the ways to get position i-1 and get position i-2
        return dp[-1]
    #time O(n)
    #space O(n)