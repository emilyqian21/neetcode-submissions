class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom up dp: time O(n) space O(n)
        n  = len(cost)
        if n < 2: 
            return 0 
        dp = [0] * (n+1) # climbing step是到达n， 但是这里是要超过n，所以要n+1
        # dp [0], dp[1] = 0, 0 

        for i in range(2,len(dp)): #len(dp) = n+1
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        return dp[-1]
