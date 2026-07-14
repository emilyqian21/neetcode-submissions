class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        water = 0
        while l < r:
            if height[l] < height[r]:
                
                left_max = max(height[l],left_max)
                water += left_max - height[l]
                l += 1
            else:
                
                right_max = max(height[r], right_max)
                water += right_max - height[r]
                r -= 1

        return water