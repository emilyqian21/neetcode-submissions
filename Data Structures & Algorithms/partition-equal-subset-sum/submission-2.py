class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    # Bottom up dp
    # Time: O(n × target)
    # Space: O(target)
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1) # dp[i] = Can I make a sum of i using the numbers I've seen so far?
        dp[0] = True

        for n in nums: 
            for s in range(target,n-1,-1): # n-1, so it stops at n. because target can't be smaller than n, then dp[s-n] will be negative
                dp[s] = dp[s] or dp[s-n]  # dp[5] Could I make sum = 5 before I started using this number?"
        return dp[target]

        #   0/1 Knapsack (use each item at most once) → iterate backwards.
        #   Unbounded Knapsack / Coin Change (reuse items unlimited times) → iterate forwards.