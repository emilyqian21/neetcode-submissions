class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        "This is a single-source shortest path problem with positive edge weights, so I use Dijkstra's algorithm.
        I build an adjacency list, then use a min heap to always expand the node with the smallest accumulated time. 
        When a node is popped for the first time, its shortest distance is finalized. 
        After processing all reachable nodes, if we haven't visited all nodes we return -1; otherwise the answer is the maximum shortest distance
        """
        node_to_neighbors = {}
        for n1, n2, w in times:
            if n1 in node_to_neighbors:
                node_to_neighbors[n1].append((n2,w)) 
            else:
                node_to_neighbors[n1] = [(n2,w)]
        
        # dijkstra's alogrithm : bfs + minheap
        heap = []
        dist = {} # node: shortest distance from starting point to this node
        heapq.heappush(heap,(0,k)) # initialize the heap with weight = 0, starting point as k 

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in dist: # if n1 already been visited and finalized the shortest distance
                continue # we continue to next round of "while"
            else:
                # it's our first time to process n1
                dist[n1] = w1 
                # add n1's neighbors to heap 
                for nei, wei_to_nei in node_to_neighbors.get(n1,[]):
                    if nei not in dist: # if we haven't processed nei before
                        heapq.heappush(heap, ( w1 + wei_to_nei,nei))

        if len(dist) < n:
            return -1
        else:
            return max(dist.values())
