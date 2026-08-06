class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time: O( n * target)
        # space: O(target)
        # There are n iterations of the outer loop. For each number, I iterate over all possible subset sums from target down to the number, which is at most target iterations. Each DP update is O(1), so the total time is O(n × target). The DP array has target + 1 entries, so the space complexity is O(target).
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2
        dp = [False] * (target + 1)
        # dp[i] = can i make a sum of i using the numbers i've seen so far?
        dp[0] = True # i can make a sum of 0 using the number i've seen so far
        for n in nums:
            for s in range(target, n-1, -1): # traverse backwards from target to n
                dp[s] = dp[s] or dp[s-n] # can i make the sum of s if i use current number or not
        return dp[target]
        # 0/1 knapsack(use each item at most once) --> iterate backwards
        # unbounded knapsack --> coin change (reuse items unlimited times) --> iterate forwards