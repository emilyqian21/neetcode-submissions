class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # time: O(amount * num of coins)
        # space: O(amount)
        coins.sort()
        dp = [0] * (amount + 1) # dp[i] = minimal coins needed for amount i
        
        for i in range(1,len(dp)):
            minn = float('inf') # we're not sure if there is a solution so set to inf
            for coin in coins:
                diff = i - coin 
                if diff < 0:
                    break
                minn = min(1 + dp[diff], minn)
            dp[i] = minn
        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]