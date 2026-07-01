class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom up dp, tabulation 
        # time : O(n)
        # space: O(n)

        # n = len(nums)
        # dp = [0] * n 
        # #edge case
        # if n == 1:
        #     return nums[0]

        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1]) # max(not rob this rob house before, rob this and two house before)

        # for i in range(2,n):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # max(not rob this rob house before = keep dp[i-1], rob this and two house before = dp[i-2] + nums[i])

        # return dp[-1]


        #space optimized
        # time: O(N)
        # space: O(1)
        n = len(nums)
        dp = [0] * n 
        #edge case
        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[0], nums[1]) # max(not rob this rob house before, rob this and two house before)

        for i in range(2,n):
            prev, curr = curr, max(curr, prev + nums[i]) # max(not rob this rob house before = keep dp[i-1], rob this and two house before = dp[i-2] + nums[i])

        return curr