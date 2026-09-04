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


        while heap:
            time, node = heapq.heappop(heap)
            if node in visit: # heap里可以有同一个node，2个不同的走法；然后短的走法已经pop过， 但长的走法也会pop，这个时候就不要加入max_time
                continue
            visit.add(node)  
            if len(visit) == n:
                return time  

            for nei, nei_w in node2nei[node]:
                if nei not in visit:
                    heapq.heappush(heap, (time + nei_w, nei)) 
                    # BFS (unweighted graph): mark visited when enqueuing.
                    #Dijkstra (weighted graph): mark visited when dequeuing (popping from the min-heap).
        return -1



        