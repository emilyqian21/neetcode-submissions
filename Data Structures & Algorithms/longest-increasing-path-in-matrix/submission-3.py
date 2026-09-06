class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # time: O (m * n)
        # space: O( m * n)
        nrow = len(matrix)
        ncol = len(matrix[0])
        memo = {} # (r,c) : longest path length at matrix[r][c]
        
        def dfs(r, c):
        # return the longest increasing path starting from matrix[r][c]
            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1

            for nr, nc in [(r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1)]:
                if (0 <= nr < nrow and 0 <= nc < ncol and matrix[nr][nc] > matrix[r][c]): # 新的cell大于现在的cell
                    longest = max(longest, 1 + dfs(nr, nc)) #比较“之前找到的最长路线” 和 “走这个 neighbor 后得到的新路线”，保留更长的。

            memo[(r, c)] = longest
            return longest

        res = 1

        for r in range(nrow):
            for c in range(ncol):
                res = max(res, dfs(r, c)) # 我把每一个 cell 都当成起点试一次，看看谁的 dfs(r,c) 最大。

        return res
                