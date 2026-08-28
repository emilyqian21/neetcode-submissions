class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        toend = [] # (index, height)

        maxarea = 0

        for i, h in enumerate(heights):
            start = i
            while toend and toend[-1][1] > h: # need to stop
                last_i, last_h = toend.pop()
                maxarea = max(maxarea, (i - last_i) * last_h)
                start = last_i

            toend.append((start, h))
        
        for i, h in toend:
            maxarea = max(maxarea, (len(heights) - i) * h)
        return maxarea
