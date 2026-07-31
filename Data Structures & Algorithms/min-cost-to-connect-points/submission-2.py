class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # prim's algo
    # 每次都计算和每个点之间的距离，然后找最近的点
    #Prim + heap version

    # Time:  O(n² log n) # 一共有n^2 edge, 每次heap操作是logn
    # Space: O(n²) 

        total = 0
        heap = [(0,0)] # distance from current point to point i, point i
        visit = set()

        while heap:
            cur_dist,cur_point = heapq.heappop(heap)
            if cur_point in visit:
                continue
            total += cur_dist
            visit.add(cur_point)

            # explore neighbors for next point move
            for i in range(len(points)):
                if i in visit:
                    continue
                dist = abs(points[i][0] - points[cur_point][0]) + abs( points[i][1] - points[cur_point][1])
                heapq.heappush(heap, (dist, i))
        return total
