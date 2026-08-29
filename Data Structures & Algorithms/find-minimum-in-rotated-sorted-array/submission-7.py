class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find lowerbound

        l = 0 
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]: # large number zone, cant be the answer. sesarch right
                l = m + 1
            else:
                r = m 
        return nums[l]
            