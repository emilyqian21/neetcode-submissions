class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [[start_index, valid_height]]
        maxArea = 0

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h: # last height smaller than current height, then can't be valid, can be determined
                last_i, last_h = stack.pop()
                maxArea = max(maxArea, last_h * (i - last_i)) # area = height * length
                #update start
                start = last_i
            # after find the start, add the current h into the stack 
            stack.append([start, h]) # the current h is valid from last_i

        
        for i,h in stack:
            maxArea = max(maxArea, h * ( len(heights) - i))
        return maxArea

