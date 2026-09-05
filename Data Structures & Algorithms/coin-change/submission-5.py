class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # dp[i] = fewest number of coins you need to make up amount i 

        dp[0] = 0

        # dp[i] = dp[i - c] + 1 
        for c in coins: # order doesn't matter, so outer
            for i in range(c, len(dp)): # unlimited usage, so forward traverse
                dp[i] = min(dp[i - c] + 1, dp[i])

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]

  