class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp definition:
        # dp[i] = 以num[i]为结尾的（包含nums[i])的 LIS长度
        
        # main logic:
        # 在nums[i] 之前的每一个数字 num[j],如果nums[j] < nums[i], 那么num[i]可以接在num[j]后面，那么dp[i] = max(dp[i], dp[j] + 1)

        # base case:
        # dp[i] = 1,因为至少LIS长度是1，自己本身就是一个LIS

        n = len(nums)
        dp = [1] * n # dp[0]...dp[len(nums) - 1]

        for i in range(len(dp)): # 0 ... len(nums) - 1
            for j in range(0,i): # 0....i - 1
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) # 易错点！不是dp[-1]，而是max!