class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bottom up dp with three states
        # time: O(n) n = len(prices)
        # space: O(1)
        # the maximum balance (profit) for each state
        hold = -float('inf') # if hold = 0, means your balance is 0 with the stock, which is not true. you need to pay to buy stock. 
        sold = 0
        rest = 0
        # at the end of every day, 3 status: 
        # hold: (stock = 1: Maximum profit at the end of today, while holding one stock.
        # sold: (stock = 0: Maximum profit at the end of today, having sold a stock today.
        # rest: (stock = 0: Maximum profit at the end of today, not holding a stock and not in cooldown (so you're free to buy tomorrow).
        for p in prices:
            # for every day, there are three status
            # How could I end today in this state?
            # hold status: to get into hold status, i can keep holding, or buy a stock to enter hold
            new_hold = max(hold, rest - p)
            # sold status: to get into sold status, i can sell a stock from hold to enter sold
            new_sold = hold + p
            # rest status: to get into rest status, i can keep in rest, or sold a stock yesterday from sold to enter rest
            new_rest = max(rest, sold)

            hold = new_hold
            sold = new_sold
            rest = new_rest

        return max(sold,rest) # cant keep "hold" because the question asks for realized profit --> the stock must be sold to have realized profit
