class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap, pop the largest
        self.large = [] # minheap, pop the smallest

    def addNum(self, num: int) -> None:
        # always add to small first
        heapq.heappush(self.small, -num)
       
        # keep valid
        if self.large:
            while -self.small[0] > self.large[0]:
                neg_too_big = heapq.heappop(self.small)
                heapq.heappush(self.large, -neg_too_big)
                
        # keep len(small) - len(large) <= 1
        while len(self.small) - len(self.large) > 1:
            max_neg = heapq.heappop(self.small)
            heapq.heappush(self.large, -max_neg)
           
        while len(self.small) < len(self.large):
            min_pos = heapq.heappop(self.large)
            heapq.heappush(self.small, -min_pos)
       
        
        
    def findMedian(self) -> float:
        # same length
        
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            print(self.small[0])
            return -self.small[0]
        