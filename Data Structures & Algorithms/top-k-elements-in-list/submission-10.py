class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # buket sort, the upper limit is set 
        bucket = [[] for _ in range(len(nums) + 1)] # bucket[0] = freq 0, bucket[6] = freq 6 

        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for n, f in counter.items():
            bucket[f].append(n)

        res = []
        for i in range(len(bucket) - 1, -1, -1): # reverse traverse
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res
        