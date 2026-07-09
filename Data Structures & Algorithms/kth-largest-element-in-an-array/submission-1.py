class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time:  O(nlogK)
        # space: O(k) ，永远只存k个元素
        #更优解是quickselect, time O(n) space O(1)
        heap = [] # minheap. pop the smallest, keep the largest
        for n in nums:
            heapq.heappush(heap,n)
            if len(heap) > k:
                heapq.heappop(heap)

        
        return heap[0]