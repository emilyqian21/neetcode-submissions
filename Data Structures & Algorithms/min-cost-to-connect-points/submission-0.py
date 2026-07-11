class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's alo
        # for each point, find the neighbor with the lowest cost. then start from that neighbor again, until the visited length = len(points)

        # adjacent dict
        point_to_neighbor = { i:[] for i in range(len(points))} # i : [ [dist, j],[dist, c]]
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i,len(points)): # all other points
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                point_to_neighbor[i].append((dist,j))
                point_to_neighbor[j].append((dist,i))

        # prim's
        res = 0
        heap = [(0,0)] # (dist, point index)
        visit = set()
        while len(visit) < len(points): # 为什么不是<=? 因为最后一次跑while应该是只差一个point没visit的时候
            dist, pt = heapq.heappop(heap)
            if pt in visit:
                continue # to next instance of "while"
            else:
                visit.add(pt)
                res += dist
                for nei_dist, nei in point_to_neighbor[pt]:
                    if nei not in visit:
                        heapq.heappush(heap, ( nei_dist,nei))
            
        return res