class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # time: O(m * n)
        # space: O( m * n)
        nrow = len(heights)
        ncol = len(heights[0])

        pacific_visited = set() # (r,c)
        pacific_q = deque()
        for c in range(ncol):
            pacific_visited.add((0,c))
            pacific_q.append((0,c))
        for r in range(nrow):
            pacific_visited.add((r,0))
            pacific_q.append((r,0))

        while pacific_q:
            r,c = pacific_q.popleft()
            for nr,nc in [( r + 1, c),(r - 1, c), (r, c + 1),(r, c -1)]:
                if nr >= 0 and nr < nrow and nc >= 0 and nc < ncol and (nr,nc) not in pacific_visited and heights[nr][nc] >= heights[r][c]:
                    pacific_q.append((nr,nc))
                    pacific_visited.add((nr,nc))

        atlantic_visited = set() # (r,c)
        atlantic_q = deque()
        for c in range(ncol):
            atlantic_visited.add((nrow - 1,c))
            atlantic_q.append((nrow - 1,c))
        for r in range(nrow):
            atlantic_visited.add((r,ncol - 1))
            atlantic_q.append((r,ncol - 1))

        while atlantic_q:
            r,c = atlantic_q.popleft()
            for nr,nc in [( r + 1, c),(r - 1, c), (r, c + 1),(r, c -1)]:
                if nr >= 0 and nr < nrow and nc >= 0 and nc < ncol and (nr,nc) not in atlantic_visited and heights[nr][nc] >= heights[r][c]:
                    atlantic_q.append((nr,nc))
                    atlantic_visited.add((nr,nc))
        return [[r,c] for r,c in atlantic_visited.intersection(pacific_visited)]


                        




