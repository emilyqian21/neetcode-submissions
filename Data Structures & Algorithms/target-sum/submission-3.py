class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # positive groups P 
        # negative groups N
        # sum(P) + sum(N) = sum(nums)
        # sum(P) - sum(N) = target
        # 2 sum(P) = sum(nums) + target
        # sum(P) = (sum(nums) + target) / 2
        # 问题就变成：求有多少个方式可以找到unique num in nums 让和等于sum(P), 剩下的num就自动变成了N组
        sum_p = (sum(nums) + target) // 2
        # print(5//2, 5/2.0) integer division (floor division), float division 写法这样比较清楚，不写.0也是float
        #edge case:
        if (sum(nums) + target) % 2 == 1: # 如果 P不是整数，比如3.5这种，就不行
            return 0
        if abs(sum(nums)) < abs(target): # 注意是abs,因为可以有负号
            return 0

        dp = [0] * (sum_p + 1)
        dp[0] = 1 # only 1 way to get sum = 0

        # each number can only use once, so reverse for loop
        for n in nums:
            for a in range(sum_p, n-1, -1):
                dp[a] = dp[a] + dp[a-n] # a-n >= 0 a >= n
        return dp[-1] 


