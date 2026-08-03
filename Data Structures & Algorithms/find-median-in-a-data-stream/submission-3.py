class MedianFinder:

    def __init__(self):
        # small (maxheap, heap[0] is the largest value); large(minheap, heap[0] is the smallest value)
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Add to max heap
        heapq.heappush(self.small, -num)

        # Step 2: Move the largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: Keep small >= large in size
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
        