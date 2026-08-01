class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time Complexity:
        # O((k + 1)(V + E)), which is commonly simplified to O(kE).

        # Space Complexity:
        # O(V)
        dist = [float('inf')] * n 
        dist[src] = 0 

        # step 2: relax 所有边 v-1次；这里因为是能停K stop,所以最多有k + 1 edge
        for _ in range( k + 1):
            update = False
            newdist = dist.copy() # 每轮copy一次

            for u, v, w in flights:
                if dist[u] == float('inf'): #目前到u还不能达到，所以不用更新了
                    continue 
                if dist[u] + w < newdist[v]: # dist代表了用i条edge到达的点，newdist代表了用 i+1条edge能到的点的距离
                    newdist[v] = dist[u] + w
                    update = True

            dist = newdist # 本轮结束，把new_dist替换掉dist
            # optimization: 如果这一轮没有update，可以提前结束 
            if not update:
                break
        
        if dist[dst] == float("inf"):
            return -1
        return dist[dst]