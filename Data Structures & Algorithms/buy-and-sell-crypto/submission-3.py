class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_profit = 0
        n = len(prices)

        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            cur_profit = max(cur_profit + diff, diff)
            max_profit = max(max_profit, cur_profit)
            
        return max_profit