class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        #edge case
        if not grid:
            return None
            
        def dfs(r,c):
            #base case: when to stop searching and return
            if r >= nrows or r < 0 or c >= ncols or c <0 or grid[r][c] != "1":
                return 
            
            #start from r,c ,explore all possibilities
            grid[r][c] = "0"
            directions = [(0,1),(0,-1),(-1,0),(1,0)]
            for d in directions:
                dfs(r+d[0],c+d[1])
            return

        count = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count

