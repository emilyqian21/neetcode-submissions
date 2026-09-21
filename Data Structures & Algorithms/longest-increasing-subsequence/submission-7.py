class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up dp (otpimal solution is binary search + greedy)
        # time: O(n^2)
        # space: O(n)
        
        # 定义： dp[i] = 以 nums[i] 结尾的最长严格递增子序列长度
        # 核心公式： if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1) 如果这个数nums[i] 比之前的数nums[j]大，那可以接在之前的数上面形成新的LIS

        n = len(nums)
        dp = [1] * n # 必须以 nums[i] 结尾的最长 increasing subsequence 长度，包含nums[i]，所以初始值都是 1。最短自己就是一个subsequence
        #dp[0] = 1
        for i in range(1,n):
            for j in range(i): # 在 i 之前的每一个数字
                if nums[i] > nums[j]: # 如果 nums[i] 大于 之前的数字nums[j]
                    dp[i] = max(dp[i], dp[j] + 1) # we don't want to reduce dp[i],so need to use max. 
        return max(dp) # 不是dp[-1] 因为 LIS 不一定以最后一个 number 结尾。


        
        # dp[i] 在问：如果我强制让 nums[i] 当最后一个数，最长能有多长？
        # nums:  1  5  2  3
        # dp:    1  1  1  1
        # 为什么都是 1？因为无论如何，每个数字自己都可以构成长度为 1 的 increasing subsequence。
        # 当 i = 1，当前数字是 5
        #我们想知道： 以 5 结尾的 LIS 最长是多少？
        # 所以我们看 5 前面的所有数字：
        # [1]  5
        #  ↑   ↑
        #  j   i

        # 1 < 5，说明：

        # 以 1 结尾的 LIS + 把 5 接到后面

        # 所以：dp[1] = dp[0] + 1 = 1 + 1 = 2
        # dp = [1, 2, 1, 1]