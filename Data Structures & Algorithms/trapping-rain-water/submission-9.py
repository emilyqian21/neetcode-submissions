class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]
        rmax = height[-1]

        l = 0 
        r = len(height) - 1
        res = 0

        while l <= r:
            if lmax < rmax:
                lmax = max(lmax, height[l])
                res += lmax - height[l]
                l += 1
                
               

            else:
                rmax = max(rmax, height[r])
                res += rmax - height[r]
                r -= 1
              

        return res