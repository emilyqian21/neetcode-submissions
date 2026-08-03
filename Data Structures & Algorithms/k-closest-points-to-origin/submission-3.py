class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            # time: O(nlogn) ,less efficient than maxheap O(nlogk)
            # space: O(n), less efficient than maxheap O(k)
        # def distance(x,y): # calculate the distance from x,y to origin(0,0)
        #     return ((x - 0)**2 + (y - 0)**2)**0.5
        
        # minheap = []
        # for x,y in points:
        #     d = distance(x,y)
        #     heapq.heappush(minheap, (d,x,y))
        # # find the smallest top k 
        # output = []
        # while len(output) < k:
        #     d,x,y = heapq.heappop(minheap)
        #     output.append([x,y])
        # return output

        # max heap
        def distance(x,y):
            return ((x - 0)**2 + (y - 0)**2)**0.5
        heap = []
        for x,y in points:
            d =  distance(x,y)
            heapq.heappush(heap,(-d,x,y))
            while len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res
