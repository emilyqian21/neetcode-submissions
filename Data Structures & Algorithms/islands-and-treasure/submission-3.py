class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # time: O(m * n)
        # space: O( m * n)
        visited = set() 
        nrow = len(grid)
        ncol = len(grid[0])

        def bfs():
            q = deque()
            
            # initialize the q with all treasures
            for r in range(nrow):
                for c in range(ncol):
                    if grid[r][c] == 0: # if this is a trasure 
                        q.append((r,c))
                        visited.add((r,c))
            # start from each treasure, start the bfs
            step = 0
            while q:
                for _ in range(len(q)): # by level
                    cur_r, cur_c = q.popleft()
                    for d_r, d_c in [(1,0),(-1,0),(0,1),(0,-1)]:
                        new_r, new_c = cur_r + d_r, cur_c + d_c
                        if (new_r >= 0 and new_r < nrow and new_c >= 0 and new_c < ncol and (new_r,new_c) not in visited and grid[new_r][new_c]!= 0 and  grid[new_r][new_c]!= -1
                    ): # valid, non visited island
                            grid[new_r][new_c] = step + 1
                            q.append((new_r, new_c))
                            visited.add((new_r,new_c))
                # this level ends
                step += 1
        return bfs()
