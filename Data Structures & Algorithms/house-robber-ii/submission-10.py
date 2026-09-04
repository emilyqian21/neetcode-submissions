class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums_to_process):
            if len(nums_to_process) == 1:
                return nums_to_process[0]

            dp = [0] * len(nums_to_process)
            dp[0] = nums_to_process[0]
            dp[1] = max(nums_to_process[0], nums_to_process[1])

            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 2] + nums_to_process[i], dp[i - 1])
            return dp[-1]
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))