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
        heapq.heappush(heap, (0,k)) # (time to arrive at node, node)
        max_time = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visit: # heap里可以有同一个node，2个不同的走法；然后短的走法已经pop过， 但长的走法也会pop，这个时候就不要加入max_time
                continue
            visit.add(node)  
            max_time = max(max_time, time) #为什么不直接return time?因为如果一个node有两个走法，第二个长的走法也会pop，也会变成time;我们需要跳过那一步的计算。

            for nei, nei_w in node2nei[node]:
                if nei not in visit:
                    heapq.heappush(heap, (time + nei_w, nei)) 
                    # BFS (unweighted graph): mark visited when enqueuing.
                    #Dijkstra (weighted graph): mark visited when dequeuing (popping from the min-heap).
        return max_time if len(visit) == n else -1



        