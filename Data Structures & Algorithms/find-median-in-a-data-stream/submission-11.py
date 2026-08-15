class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:

        # 1. add into small heap --> max heap --> small[0] is largest
        heapq.heappush(self.small, -num)
       
    
        # 2. move the largest of the small into large
        heapq.heappush(self.large, -1 * heapq.heappop(self.small))
       

        # 3. if len(small) < len(large), move the smallest value of the large to small
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))
           

    def findMedian(self) -> float:
        # if len(small) > len(large), return small[0]
        if len(self.small) > len(self.large):
            return -1 * self.small[0] # 易错点：这里不用pop，只需要查看就行
        # if len(small) == len(large), return the average
        else:
        
            left = -1 * self.small[0]
            right = self.large[0]
            return (left + right) / 2.0
        
        