class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         #bottom up dp (tabulation)
#         #time: O(amount * coin)
#         # spacE: O(amount)
        coins = sorted(coins)

        dp = [0] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            min_coins = float("inf")

            for coin in coins:
                diff = i - coin

                if diff < 0:
                    break

                min_coins = min(min_coins, dp[diff] + 1) # 用满足diff的coin + 用这个coin = total coin number

            dp[i] = min_coins

        if dp[amount] < float("inf"):
            return dp[amount]
        else:
            return -1



