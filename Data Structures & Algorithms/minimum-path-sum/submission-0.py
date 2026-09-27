class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp defnition: dp[r][c] = minimum path sum from [0][0] to [r][c]
        # main logic: dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
        nrow = len(grid)
        ncol = len(grid[0])
        dp = [[float('inf')] * ncol for _ in range(nrow)]
    

        # base case
        dp[0][0] = grid[0][0]
        for c in range(1, ncol): # first row
            print(c, c - 1)
            dp[0][c] = dp[0][c - 1] + grid[0][c]
        for r in range(1, nrow): # first column
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # transition
        for r in range(1, nrow):
            for c in range(1, ncol):
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1] 