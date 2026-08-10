class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #counter
        count = {} # num, frequency
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # heap
        heap = [] # store (frequency, num)
        for n, f in count.items():
            heapq.heappush(heap, (f,n))
            if len(heap) > k:
                heapq.heappop(heap)

        
        res = []
        for f,n in heap:
            res.append(n)
            
        return res
    