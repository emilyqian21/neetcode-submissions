class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [ [] for i in range(len(nums) + 1)] # bucker[0] -> freq 0, bucker[6] -> freq 6

        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for n, f in counter.items():
            bucket[f].append(n) # bucket[2] --> [4,5]--> both 4 and 5 showed up twice

        res = []
        for i in range(len(bucket) - 1, -1, -1): # reverse traverse
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

