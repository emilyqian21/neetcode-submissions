class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)  # 易错点：heapify是直接inplace修改，是return None的
        # 优化点：在init的时候就维护heap <= k 
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        # 1. add into the heap
        heapq.heappush(self.heap, val)
        # 2. pop 
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # 3.return kth largest value
        return self.heap[0] # the top of the minheap is the smallest 