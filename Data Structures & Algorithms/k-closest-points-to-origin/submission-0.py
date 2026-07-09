class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for p_x, p_y in points:
            dist = ((p_x ** 2) + (p_y ** 2)) ** 0.5
            maxheap.append((-1 * dist,p_x,p_y))
        heapq.heapify(maxheap) # maxheap[0] is the pair with ( largest abs distance, p_x, p_y )
        
        while len(maxheap) > k:
            heapq.heappop(maxheap)
        res = []
        for neg_dis, p_x, p_y in maxheap:
            res.append([p_x,p_y])
        return res
