class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane's algo
        max_profit = 0
        cur_profit = 0

        for i in range(1,len(prices)):
            change = prices[i] - prices[i - 1]
            cur_profit = max(cur_profit + change, change) # continue the path or start fresh
            max_profit =  max(max_profit, cur_profit)
        return max_profit