class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxamount = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            curamount = (r - l) * min(heights[l], heights[r])
            maxamount = max(maxamount, curamount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxamount