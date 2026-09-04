class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1) # dp[i] = minimal cost to reach stair i ; last posiiton is minimal cost to reach stair i + 1, pass i 

        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[0] + cost[1], cost[0], cost[1])

        for i in range(3, len(dp)):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]