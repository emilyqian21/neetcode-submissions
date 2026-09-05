class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {0: 0}
        def dfs(amount):
            # return the minimum number of coins needed to get to amount 'amount'
            if amount in memo:
                return memo[amount]
            
            min_coins_needed = float('inf')

            for c in coins:
                if amount < c:
                    continue
                cur_coins_needed = dfs( amount - c) + 1
                min_coins_needed = min(min_coins_needed, cur_coins_needed)
                memo[amount] = min_coins_needed
            
            return min_coins_needed
        res = dfs(amount)
        if res == float('inf'):
            return -1 
        else:
            return res