class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #dfs, start from the oceans. 
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

        for c in range(ncol): # start from the first  and last row 
            dfs(0,c,pac,heights[0][c]) # firs row: start from pacific ocean
            dfs(nrow - 1, c, atl, heights[nrow - 1][c]) # last row: start from atlantic ocean

        for r in range(nrow): # start from the first and last column
            dfs(r,0,pac,heights[r][0])  # first column: start from pacific ocean
            dfs(r, ncol - 1, atl, heights[r][ncol - 1]) # last column: start from atlantic ocean
        
        # traverse each cell in the grid
        for r in range(nrow):
            for c in range(ncol): 
                if (r,c) in pac and (r,c) in atl: # if the cell is in both pacific and atlantic sets, it can reach both coean. so append it
                    res.append([r,c])

        return res

        #time: O(m *n)
        #space: O(m *n)
