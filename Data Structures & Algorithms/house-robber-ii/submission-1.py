class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            # dp = [0] * n
            # dp[0] = nums[0]
            # dp[1] = max(nums[1],dp[0])
            # for i in range(2,n):
            #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            # return dp[-1]
            prev = nums[0]
            curr = max(nums[1], prev)
            for i in range(2,n):
                prev, curr = curr, max(curr, prev + nums[i])
            return curr
        n = len(nums)
        #edge case
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        return max(helper(nums[:n-1]), helper(nums[1:]))
