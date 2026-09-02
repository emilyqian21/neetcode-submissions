class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        self.maxarea = 0
        visited = set()
        self.curarea = 0

        def dfs(r, c):
            # return the area of island start from grid[r][c]
            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r, c) in visited or grid[r][c] != 1:
                return 0
            
            # choose
            visited.add((r, c))
            self.curarea += 1

            # explore
            for nr, nc in [(r + 1, c), ( r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(nr, nc)
        
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1 and (r, c) not in visited:
                    self.curarea = 0
                    dfs(r,c)
                    self.maxarea = max(self.maxarea, self.curarea)
        return self.maxarea
            
            

