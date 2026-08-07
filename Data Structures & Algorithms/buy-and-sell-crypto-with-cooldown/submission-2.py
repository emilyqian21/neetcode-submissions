class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # time: O(n) n = len(prices)
        # space: O(1)

        # bottom up dp with three states
        # hold = max profit if I'm currently holding a stock
        # sold = max profit if I sold today
        # rest = max profit if I'm not holding and didn't sell today

        hold = -prices[0] # we pay the price[0] to buy the stock so netprofit is negative
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            # for every day, there are three status
            # How could I end today in this state?

            # keep holding OR buy today
            hold = max(prev_hold, prev_rest - price)

            # must sell the stock we held yesterday
            sold = prev_hold + price

            # keep resting OR enter cooldown after selling yesterday
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)