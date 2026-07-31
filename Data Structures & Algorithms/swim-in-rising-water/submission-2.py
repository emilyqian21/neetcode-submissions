class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # djikstra's alog
        heap = [] # (maxheight, r, c)
        nrow = len(grid)
        ncol = len(grid[0])
        visit = set()
        #initialize queue
        heapq.heappush(heap, (grid[0][0],0,0)) #易错点：初始是 grid[0][0]，不是0
        res = 0

        while heap:
            path_max, r, c = heapq.heappop(heap)
            if (r,c) in visit:
                continue
            visit.add((r,c))  # 第一次 pop 出来的未访问节点，是当前真正的最优值。所以才放入visit
            res = path_max
            if (r,c) == (nrow - 1, ncol - 1):
                return res

            # add neighbor
            for nr,nc in [(r + 1, c), (r - 1, c), ( r, c + 1), ( r, c -1)]:
                if nr >= 0 and nr < nrow and nc >= 0 and nc < ncol and (nr,nc) not in visit:
                    heapq.heappush(heap, ( max(grid[nr][nc], path_max) ,nr, nc))
                    
