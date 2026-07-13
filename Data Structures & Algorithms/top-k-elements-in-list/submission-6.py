import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency有上限
        bucket = [ [] for i in range(len(nums) + 1)] # index of bucket就是出现的frequency

        count = collections.Counter(nums)
        print(count)
        for n, f in count.items():
            bucket[f].append(n) # bucket[1] = [3,4]
        
        # loop thru the bucket from largest to smallest. if equal to k, then return
        res = []
        for b in range(len(bucket)-1, -1, -1):
            res.extend(bucket[b])
            if len(res) == k:
                return res

