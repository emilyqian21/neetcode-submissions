class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0] * (n + 1)
        
        # for i in range(2,len(dp)):
        #     dp[i] = min( dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        # return dp[-1]

        n = len(cost)
        cur = 0
        prev = 0

        for i in range(2,n + 1):
            prev, cur = cur, min( prev + cost[i - 2], cur + cost[i - 1])
        return cur