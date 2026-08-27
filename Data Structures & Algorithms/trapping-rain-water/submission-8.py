class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]
        rmax = height[-1]

        l = 0 
        r = len(height) - 1
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
                
               

            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
                
              

        return res