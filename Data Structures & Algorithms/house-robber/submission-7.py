class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) # option1 steal option2 not steal
        return dp[-1]
