class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        max_count = 0

        def dfs(r,c):
            #base case
            if r >= nrows or r < 0 or c >= ncols or c < 0 or grid[r][c] !=1:
                return 0
            
            #explore all possibilities
            #current position
            grid[r][c] = 0
         
            #continue this path by exploring the following possibilities
            # area = current node + up + down + right + left
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r, c-1)
            

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    max_count = max(dfs(r,c),max_count)

        return max_count
                    