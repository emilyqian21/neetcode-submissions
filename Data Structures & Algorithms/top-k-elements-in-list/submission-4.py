import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # #bucket sort
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1 #nums = [1,1,1,1] or [1,1,2,3]
        bucket = [[] for _ in range(len(nums)+1)] #[[],[],[],[]], index是指frequency
        
        for n,f in count.items():
            bucket[f].append(n)

        res = []
        for  i in range(len(bucket)-1, 0, -1):
            for x in bucket[i]:
                res.append(x)
                if len(res)==k:
                    return res
    #time: O(n)
    #space: O(n)
        # # minheap
        # count = Counter(nums)
        # heap = []
        # if count:
        #     for n,f in count.items():
        #         heapq.heappush(heap,(f,n))
        #         if len(heap)>k:
        #             heapq.heappop(heap)
        # res = []
        # for i in heap:
        #     res.append(i[1])
        # return res
# Time:O(Nlogk) heap就是logk, 遍历n个number，所以是nlogk
# Space: O(n+k), n就是numbers, k就是top k 
'''
The Counter stores all unique elements, which requires O(M) space where M is the number of distinct values. 
The heap stores at most k elements, requiring O(k) space. 
Therefore the total space complexity is O(M + k). 
In the worst case where every element is unique, 
M = N, so it becomes O(N + k), which simplifies to O(N)
'''



