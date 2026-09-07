class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp definition: dist[v] = minimum cost from node src to node v
        # main logic: K stops → K+1 edges；每轮多允许一条 edge,看看能不能更新dist[v]；上一轮 dist 读、这一轮 newdist 写，防止同一轮连续走多条边。

        # using at most the currently allowed number of edges
        dist = [float("inf")] * n    # dist[v] = minimum cost from src to v
        dist[src] = 0

        # k stops = at most k + 1 edges
        for _ in range(k + 1):
            newdist = dist.copy()

            for u, v, price in flights:
                if dist[u] == float("inf"): #dist[u] == float('inf')表示如果目前还没有办法从 src 到达 u，那就没法通过 u -> v 去更新 v
                    continue # 所以跳过

                newdist[v] = min(newdist[v], dist[u] + price) # 看看加一个edge，从 u --> v 和已经存的到v的distance,哪个更短

            dist = newdist

        return -1 if dist[dst] == float("inf") else dist[dst]