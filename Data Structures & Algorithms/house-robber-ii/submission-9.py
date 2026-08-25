class Solution:
    def rob(self, nums: List[int]) -> int:
        def houserob_helper(i,j): # nums[i:j]
            h = nums[i:j]
            # edge case
            if not h:
                return 0
            if len(h) == 1:
                return h[0]

            dp = [0] * len(h)
            dp[0] = h[0]
            dp[1] = max(h[0], h[1])
            for i in range(2, len(dp)):
            # main logic
                dp[i] = max(dp[i - 2] + h[i], dp[i - 1])
            return dp[-1]
        
        # edge case
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(houserob_helper(0, len(nums) - 1), houserob_helper(1, len(nums)))
            