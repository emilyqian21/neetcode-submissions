class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # time: O (n^3) there're at most n^2 subarray, and we run n for each of the subarray
        # sapce o (n^2) there are at most n^2 subarray(O(n²) possible intervals (l, r).)
        nums = [1] + nums + [1] # add 1 both before and after the nums
        dp = {} # save (l,r) max coins

        def dfs(l,r):
            # base case
            if l > r:
                return 0 
            if (l,r) in dp:
                return dp[(l,r)]
            
            # process the cur node
            dp[(l,r)] = 0 # initialize as 0 
            for i in range(l, r + 1): # loop thru every position from l to r 
                coins = nums[l - 1] * nums[i] * nums[ r + 1] # we pop i last, so 1[i]1, l-1 ->1  r - 1> 1
                coins += dfs(l, i - 1) + dfs(i + 1, r) # left subarray and right subarray
                dp[(l,r)] = max(dp[l,r], coins) # dfs(l, r) needs to remember the best answer among all possible choices of i
            return dp[(l,r)]
        
        return dfs(1, len(nums) - 2)