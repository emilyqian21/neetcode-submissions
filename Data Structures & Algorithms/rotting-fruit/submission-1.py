class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        q = deque()
        fresh = 0
        time = 0 


        # first, find the rotten oranages, add them into the q; find the number of fresh oranges
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2: 
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # second, bfs with multiple start 
        while q and fresh > 0: # if fresh == 0 ,early stop
            for _ in range(len(q)): # each level; first level is rotten oranges
                r,c = q.popleft()
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_r, new_c = r + d[0], c + d[1]
                    if (new_r >= nrow or new_r < 0 or new_c >= ncol or new_c < 0 or grid[new_r][new_c] != 1): # skip outbond/not fresh oranges
                        continue
                    else: # inbound and fresh oranges
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        fresh -= 1
            #end of this level
            time += 1
        
        # return res
        if fresh == 0:
            return time
        else: 
            return -1

        # time: O(m*n)
        # spcae: O(m*n)
