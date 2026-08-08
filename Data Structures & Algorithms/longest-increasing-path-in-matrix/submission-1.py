class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        dp = {} # (r,c) : longest path length at matrix[r][c]
        
        def dfs(r,c,prev):
            # base case
            if r < 0 or r >= nrow or c < 0 or c >= ncol or matrix[r][c] <= prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            res =  1 + max(dfs(r + 1, c, matrix[r][c]), dfs(r - 1, c, matrix[r][c]), dfs(r, c + 1, matrix[r][c]), dfs(r , c - 1, matrix[r][c]))
            dp[(r,c)] = res #易错点：一定要存dp!
            return res

        max_res = 1
        for r in range(nrow):
            for c in range(ncol):
                max_res = max(max_res, dfs(r,c, -float('inf')))
        return max_res
                