class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up dp (otpimal solution is binary search + greedy)
        # time: O(n^2)
        # space: O(n)
        n = len(nums)
        dp = [1] * n
        #dp[0] = 1
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # we don't want to reduce dp[i],so need to use max. 
        return max(dp)