class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up dp
        # time: O(n * m) n = num of coins, m = amount, two for loops
        # space: O(m) 
        dp = [0] * (amount + 1) #dp[i] = 凑到amount = i 的unique的方法数； dp = [0,0,....0] 最后的index是amount，比如amout = 8，那最后index = 8,因为长度是8+1
        dp[0] = 1 # 凑到amount = 0只有一种方法，就是什么都coin都不用

        for c in coins: # coin 在外层，因为我们可以避免出现 121 和 112 重复的情况；我们都是先loop完1，再loop完2 ...
            for a in range(c,amount+1): #要保证 a-c >= 0
                dp[a] = dp[a] + dp[a - c] # 现在已经有的方法数量 + 新的通过加这个coin能凑到amount的方法数量
        return dp[-1] 
 


        #正序：能看到自己刚更新的新状态 → 可以继续接着用自己 → 无限次使用（Complete Knapsack）
        #倒序：只能看到旧状态，看不到自己刚更新的新状态 → 最多使用一次（0/1 Knapsack）