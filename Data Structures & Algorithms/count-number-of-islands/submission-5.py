class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0 
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def dfs(r, c):
            # traverse style - traverse all island from grid[r][c]
            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r, c) in visited or grid[r][c] != "1":
                return
            #choose
            visited.add((r, c))
            # explore
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(nr, nc)
            

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    self.count += 1

        return self.count
