class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra's algo: shortest path with weight, bfs with minheap
        # time: O ( Elogv)
        # space: O ( V + E)

        node2nei = defaultdict(list)
        for u,v,t in times:
            node2nei[u].append((v,t)) # node: (neighbor node, weight)
        
        heap = []
        visit = set()
        heapq.heappush(heap, (0,k)) # (time, node)
        max_time = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            max_time = max(max_time, time)

            for nei, nei_w in node2nei[node]:
                if nei not in visit:
                    heapq.heappush(heap, (time + nei_w, nei)) 
                    # BFS (unweighted graph): mark visited when enqueuing.
                    #Dijkstra (weighted graph): mark visited when dequeuing (popping from the min-heap).
        return max_time if len(visit) == n else -1



        