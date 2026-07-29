class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # time: O(m * n)
        # space: O( m * n)
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def bfs():
            q = deque()
            # initialize the q with all rotten fruits
            for r in range(nrow):
                for c in range(ncol):
                    if grid[r][c] == 2:
                        q.append((r,c))
                        visited.add((r,c))


            # now the q has all rotten fruits locations. start the bfs traverse
            time = 0 

            while q:
                for _ in range(len(q)): # travere by level
                    r,c = q.popleft()
                    for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if (new_r >= 0 and new_r < nrow and new_c >=0 
                        and new_c < ncol and (new_r, new_c) not in visited and grid[new_r][new_c] == 1
                        ): # if valid cell and the cell is fresh fruit
                            grid[new_r][new_c] = 2 # fresh became rotten
                            q.append((new_r, new_c))
                            visited.add((new_r, new_c))
                # end of this level
                # add time only if there is new oranges added
                if q:
                    time += 1
            return time

        totaltime = bfs()
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    return -1

        return totaltime
