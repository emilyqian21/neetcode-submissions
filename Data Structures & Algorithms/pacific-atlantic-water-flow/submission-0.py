class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        nrow = len(heights)
        ncol = len(heights[0])
        res = []

        def dfs(r,c,visited, prev_height):
            # base case: when can't proceed and  have to return 
            if r >= nrow or r < 0 or c >= ncol or c < 0 or (r,c) in visited or heights[r][c] < prev_height:
                return

            visited.add((r,c))
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_r, new_c = r + d[0], c + d[1]
                dfs(new_r,new_c,visited, heights[r][c])
            return

        for c in range(ncol):
            dfs(0,c,pac,heights[0][c])
            dfs(nrow - 1, c, atl, heights[nrow - 1][c])

        for r in range(nrow):
            dfs(r,0,pac,heights[r][0]) 
            dfs(r, ncol - 1, atl, heights[r][ncol - 1])
        
        for r in range(nrow):
            for c in range(ncol):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
