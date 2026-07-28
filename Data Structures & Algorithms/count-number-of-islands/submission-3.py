class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def dfs(r,c): # return 
            # base case
            if r < 0 or r >= nrow or c < 0 or c >= ncol or grid[r][c] != "1" or (r,c) in visited:
                return 
            
            # process current cell
            visited.add((r,c))

            #explore other directions continuing this path
            for new_r, new_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(new_r, new_c)
            return
        
        count = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
        return count