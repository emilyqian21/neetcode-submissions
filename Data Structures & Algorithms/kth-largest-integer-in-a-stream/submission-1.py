class KthLargest:
# time:  # heapify: O(n); pop: O((n-k)logn) ,# total O(nlogn)
# space: O(k), heap里面最多k个元素
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums) # heapify return的是none, 是in-place change, nums已经变成heap了
        self.minheap = nums
        if len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
