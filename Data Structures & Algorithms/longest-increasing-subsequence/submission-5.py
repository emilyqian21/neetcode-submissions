class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up dp (otpimal solution is binary search + greedy)
        # time: O(n^2)
        # space: O(n)
        n = len(nums)
        dp = [1] * n # 必须以 nums[i] 结尾的最长 increasing subsequence 长度，包含nums[i]，所以初始值都是 1。最短自己就是一个subsequence
        #dp[0] = 1
        for i in range(1,n):
            for j in range(i): # 在 i 之前的每一个数字
                if nums[i] > nums[j]: # 如果 nums[i] 大于 之前的数字nums[j]
                    dp[i] = max(dp[i], dp[j] + 1) # we don't want to reduce dp[i],so need to use max. 
        return max(dp) # 不是dp[-1] 因为 LIS 不一定以最后一个 number 结尾。