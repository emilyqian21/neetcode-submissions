class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom up dp
        # time:
        # space:
        # m is nrow
        # n is the ncol
        dp = [1] * n # the first top row; dp[i] = the number of ways to reach the destination in the ith column in current row 
        for i in range(1,m): # start looping from the second row to the last row(inclusive)
            for j in range(1,n): # each column
                dp[j] = dp[j-1] + dp[j] # dp[j-1] = left cell of current cell, dp[i] = last row's current column --> cell above current cell
        
        return dp[-1]  