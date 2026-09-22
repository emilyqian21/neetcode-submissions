class Solution:
    def numSquares(self, n: int) -> int:
        # dp definition:
        # dp[i] = the minimum perfect-square-number(coin) needed to sum up to amount i 
        # main logic:
        # dp[i] = min(dp[i], dp[i - coin] + 1)

        # base case
        # dp[0] = 0

        dp = [float('inf')] * (n + 1) # dp[0]...dp[n]
        coins = [] # [1,4,9...]
        # base case
        dp[0] = 0 

        i = 1
        while i * i <= n:
            coins.append(i * i)
            i += 1

        for c in coins:
            for i in range(c, n + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1]