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

            if len(shortest) == n:
                return w1

            # add neighbors
            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (w1 + w2, n2))
        
        if len(shortest) != n:
            return -1
