class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def dfs(r,c): # return area
            # base case
            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r,c) in visited or grid[r][c] != 1:
                return 0
            
            # process current cell
            visited.add((r,c))
            left_area = dfs( r, c - 1)
            right_area = dfs( r, c + 1)
            up_area = dfs(r - 1, c)
            down_area = dfs( r + 1, c)
            cur_area = left_area + right_area + up_area + down_area + 1
            return cur_area
            # for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r , c -1)]:
            #     area += dfs(new_r, new_c)

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1 and (r,c) not in visited:
                    self.max_area = max(self.max_area, dfs(r,c))
        return self.max_area