class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_profit = 0

        for i in range(len(prices)):
            if i == 0:
                change = 0
            
            else:
                change = prices[i] - prices[i-1]
            cur_profit = max(cur_profit + change,  change)
            max_profit = max(max_profit, cur_profit)
        
        return max_profit

        #time: O(N)
        #space: O(1)