class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

    #Time: O(nP)→ n numbers × P DP states -->We iterate through each number once, and for each number, we iterate backward through the DP array up to P.
    # Space: O(P)→ one 1D DP array   P = (sum(nums) + target) / 2

        # 变成 num of ways to find subsum = 一个特定的数(P)
        #原理： P + N = total, P - N = target P = (total + target)//2 

        # edge case
        if abs(target) > abs(sum(nums)):
            return 0 
        p = (sum(nums) + target)//2
        if (sum(nums) + target) % 2 != 0:
            return 0
        
        dp = [0]*(p + 1) # dp[i] = num of ways to get sum equal to i
        dp[0] = 1 #有一种方式凑成0
        for n in nums: # 外层loop是n, 对于每一个 n，决定它要不要加入当前 subset,不用倒序
            for s in range(p,n-1,-1): # traverse backward, because every number can only use once
            #为什么从 p 开始？
            #→ dp 最大只需要算到 p
            # 为什么到 n 为止？
            # → 保证 s - n >= 0
            # 为什么倒着走？
            # → 防止当前 n 被重复使用
                dp[s] = dp[s] + dp[s - n] # 凑出 s 的方法数=原本凑出 s 的方法数+用了当前 n 以后新增的方法数
        return dp[-1]


        #0/1 knapsack:每个物品只能选 0 次或者 1 次。
        # number 在外层
        #sum 在内层，并且倒序