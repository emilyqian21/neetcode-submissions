class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque([])
        nrow = len(grid)
        ncol = len(grid[0])
        # find all treasures to q
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # from treasures, bfs 
        step = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] != 0:
                    grid[r][c] = step
                    print(step) 

                for nr, nc in [(r + 1, c), (r - 1, c), (r , c + 1), (r, c - 1)]:
                    if nr >= 0 and nr < nrow and nc >= 0 and nc < ncol and (nr, nc) not in visited and grid[nr][nc] != -1:
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))
            step += 1
            print("aftet step += 1", step)
        
        return 
