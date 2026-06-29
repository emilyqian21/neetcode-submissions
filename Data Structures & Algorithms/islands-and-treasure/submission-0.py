class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    #bfs, start from the gate(treasure chest) simultaneously
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        q = deque([])
        
        #first, save all the doors in the queue
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                       
        #second, from each door, start bfs simultaneously
        distance = 0
        while q:
            for _ in range(len(q)): # traverse each level. the first level is the door, second is 1 step from door
                r,c = q.popleft()
                
                grid[r][c] = distance # first layer is door, default distance is 0 
                
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_r, new_c = r+d[0], c+d[1]
                    if (new_r >= nrow or new_r < 0 or new_c >= ncol or new_c < 0 
                        or (new_r,new_c) in visited or grid[new_r][new_c] == -1):
                        continue 
                    else:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
            distance += 1 #after each layer(level),distance += 1
        return 