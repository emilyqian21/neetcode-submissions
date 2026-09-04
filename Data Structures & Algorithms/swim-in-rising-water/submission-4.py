class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # djikstra's alog
        # Time: O(V log V + E log V) 
        # 对于这题：V = n² , E = 4n² = O(n²) 
        # 代进去得出： O((V + E) log V) = O(n² log(n²)) = O(n² log n)

        # Space Complexity: O(n²)
        # - O(n²) for the visited set.
        # - O(n²) for the min-heap in the worst case.
        
        # Dijkstra 永远先探索当前成本最低的候选路线。
        # 在network delay time中， new_cost = current_cost + edge_time
        # 在swim in the rising water中， new_cost = max(current_cost, next_height)
        # heap存的是（new_cost, r, c）
        heap = [] # (maxheight, r, c)
        nrow = len(grid)
        ncol = len(grid[0])
        visit = set()
        #initialize queue
        heapq.heappush(heap, (grid[0][0],0,0)) #易错点：初始是 grid[0][0]，不是0
      

        while heap:
            path_max, r, c = heapq.heappop(heap)
            if (r,c) in visit:
                continue
            visit.add((r,c))  # 第一次 pop 出来的未访问节点，是当前真正的最优值。所以才放入visit
    
            if (r,c) == (nrow - 1, ncol - 1):
                return path_max # 到最后一个格子了，就可以return了

            # add neighbor
            for nr,nc in [(r + 1, c), (r - 1, c), ( r, c + 1), ( r, c -1)]:
                if nr >= 0 and nr < nrow and nc >= 0 and nc < ncol and (nr,nc) not in visit:
                    heapq.heappush(heap, ( max(grid[nr][nc], path_max) ,nr, nc))
                    
