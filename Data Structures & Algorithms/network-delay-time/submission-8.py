class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        # dijkstra: weighted nonnegative edge, find shortest path with weight
        adj = defaultdict(list)
        for n1, n2, t in times:
            adj[n1].append((t,n2))

        heap = [(0,k)] # （total weight from src to current node, current node)
        shortest = {}

        while heap:

            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            if len(shortest) == n: # 易错点：这个不要放在一开始检查，而是要更新完w1后再检查，因为有可能是heap pop空了， shortest == n, 如果写在之前，那么while heap不满足， return就永远不会被执行
                return w1

            # add neighbors
            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (w1 + w2, n2))
        
        if len(shortest) != n:
            return -1
