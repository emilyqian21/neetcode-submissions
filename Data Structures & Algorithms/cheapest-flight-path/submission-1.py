class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra with k stops
        # time: O(EK log(EK)) # E = number of flights, k = maximum flights
        # space: O(VK + E) # V(nodes) = number of cities
        # best 记录 (cost,node, stops)
        # 每次都找状态（node，stops) 最便宜的,然后更新到best里

        # step 1: adjacent graph
        node_to_nei = collections.defaultdict(list)
        for n1, n2, cst in flights:
            node_to_nei[n1].append((cst,n2))
        
        # step 2: modified dijkstra with k stops
        best = {} # state(node, stop) : cost
        heap = [(0,src,0)] # (cost, node, stop)

        while heap:
            cost, node, stop = heapq.heappop(heap)
            if node == dst:
                return cost

            if stop > k:
                continue
            else:
                if (node, stop) not in best or  best[(node,stop)] > cost:
                    best[(node, stop)] = cost # update the best
                else:
                    continue # skip this round, continue with  next instance in while

                for nei_cost, nei in node_to_nei[node]:
                    heapq.heappush(heap, (nei_cost + cost, nei, stop + 1))
        return -1 