class MedianFinder:

    def __init__(self):
        # small (maxheap, heap[0] is the largest value); large(minheap, heap[0] is the smallest value)
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. add the num
        if self.small and  (-1 * self.small[0]) < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        # 2. check and organize tthe heaps
        while self.small and self.large and (-1 * self.small[0]) > self.large[0]: # the largest value in small is bigger than the smallest value in large
            pos_val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, pos_val)

        while len(self.small) - len(self.large) > 1:
            pos_val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, pos_val)

        while len(self.large) - len(self.small) > 1:
            pos_val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * pos_val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0
        