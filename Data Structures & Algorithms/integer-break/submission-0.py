class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] = maximum product after breaking amount i into at least two positive integers
        dp = [0] * (n + 1) # because we need the i = 0....n 

        # base case
        dp[0] = 0  # both 1 and 0 can't be split into k positive integers. so maximum product remains 0
        dp[1] = 0

        for num in range(2, n + 1):
            for first in range(1, num): # range of possible postive integers. for each num, we try all the split possibilities
                remaining = num - first
                # Either:
                # 1. Don't break remaining: first * remaining
                # 2. Break remaining further: first * dp[remaining]
                dp[num] = max(dp[num], first * remaining, first * dp[remaining]) # why we need dp[nums] in max? because there are multiple spliting ways (remainings), we need to keep the best answer

        return dp[-1]