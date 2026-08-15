class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. add to small. small[0] is the largest --> maxheap --> save -1 *num
        heapq.heappush(self.small, -num)

        # 2. move the largest value of small to large
        heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # 3. if len(small) < len(large), move the smallest value from large to small
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        # if same length, return average
        if len(self.small) == len(self.large):
            left = -1 * self.small[0]
            right = self.large[0]
            return (left + right) / 2

        # elif len(self.small) > len(self.large), return the largest value of small
        else:
            return -1 * self.small[0]
        
        