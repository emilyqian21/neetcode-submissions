class StockSpanner:
    # solution: monotonic decreasing stack 
        # 1. stack 存 (price, span)
        # 2. 当前 price >= stack top price
        #    → pop
        #    → absorb its span
        # 3. stack 保持 decreasing prices
        # 和temperature的区别：都是monotonic decreasing stack, 但是temperature 是找next greater value；这个题是看past smaller value

    def __init__(self):
        self.stack = [] # 存(price, span)
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)