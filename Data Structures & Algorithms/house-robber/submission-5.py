class Solution:
    def rob(self, nums: List[int]) -> int:
        # #bottom up dp (tabulation)
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0],nums[1])
        
        # dp = [0] * n # dp[i] -> the max money can be robbed at position i 
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,n):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1]) # max(rob the house, not rob the house)
        # return dp[-1]

        # bottom up dp(constant space)
        # time : O(n)
        # space: O(1)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
      
        prev = nums[0] # money two steps back
        curr = max(nums[0],nums[1]) # money one step back
        for i in range(2,n):
            prev, curr = curr, max(prev + nums[i], curr) # max(rob the house, not rob the house)
        return curr