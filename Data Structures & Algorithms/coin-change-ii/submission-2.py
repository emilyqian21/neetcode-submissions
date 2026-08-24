class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) # dp[i] = num of ways to get amount i 

        dp[0] = 1 
        
        for coin in coins:
            for i in range(coin, amount + 1):
                diff = i - coin
                dp[i] = dp[i] + dp[diff]
        return dp[-1]