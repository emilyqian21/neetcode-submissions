class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nrow = len(heights)
        ncol = len(heights[0])

        pacific_visited = set()
        pacific_q = deque([])
        # first row
        for c in range(ncol):
            pacific_q.append((0,c))
            pacific_visited.add((0,c))
        # first column
        for r in range(nrow):
            pacific_q.append((r,0))
            pacific_visited.add((r,0))

        while pacific_q:
            r, c = pacific_q.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c  - 1)]:
                if (nr >= 0 and nr < nrow and nc >= 0 
                    and nc < ncol and (nr, nc) not in pacific_visited 
                    and heights[nr][nc] >= heights[r][c] ): # valid
                    pacific_q.append([nr, nc])
                    pacific_visited.add((nr, nc))
        print ("p:", pacific_visited)

        #atlantic   
        atlantic_visited = set()     
        atlantic_q = deque([])
        # last row
        for c in range(ncol):
            atlantic_q.append((nrow - 1,c))
            atlantic_visited.add((nrow - 1,c))
        # last column
        for r in range(nrow):
            atlantic_q.append((r, ncol - 1))
            atlantic_visited.add((r, ncol - 1))
        print("A:", atlantic_visited)

        while atlantic_q:
            r, c = atlantic_q.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c  - 1)]:
                if (nr >= 0 and nr < nrow and nc >= 0 
                    and nc < ncol and (nr, nc) not in atlantic_visited 
                    and heights[nr][nc] >= heights[r][c]): # valid
                    atlantic_q.append([nr, nc])
                    atlantic_visited.add((nr, nc))
        res = pacific_visited.intersection(atlantic_visited)
        # print ("a", atlantic_visited)
        return list(res)
        