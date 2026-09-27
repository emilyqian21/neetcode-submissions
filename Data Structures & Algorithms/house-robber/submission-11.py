class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n # dp[i] = max amount you can rob at house i 

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
