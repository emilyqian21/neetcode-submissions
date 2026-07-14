class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        left_max = 0
        right_max = 0
        
        water = 0
        
        while l < r:
            
            if height[l] < height[r]:
                # left side is limiting the water level
                
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                
                l += 1
                
            else:
                # right side is limiting the water level
                
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                
                r -= 1
        
        return water