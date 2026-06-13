import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        if count:
            for n,f in count.items():
                heapq.heappush(heap,(f,n))
                if len(heap)>k:
                    heapq.heappop(heap)
        res = []
        for i in heap:
            res.append(i[1])
        return res

